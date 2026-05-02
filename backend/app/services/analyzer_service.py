import json
import subprocess
from pathlib import Path
from radon.complexity import cc_visit
from app.utils.file_utils import list_code_files, safe_read


class AnalyzerService:
    def analyze(self, root: Path) -> tuple[int, list[dict]]:
        findings: list[dict] = []
        files = list_code_files(root)

        if not files:
            findings.append({
                "category": "repository",
                "severity": "high",
                "file": None,
                "message": "Nenhum arquivo de código suportado foi encontrado.",
                "recommendation": "Confirme se o repositório possui código-fonte em linguagens suportadas."
            })
            return 45, findings

        findings.extend(self._static_checks(root, files))
        findings.extend(self._python_complexity(files))
        findings.extend(self._bandit_scan(root))

        penalty = sum(self._severity_penalty(f["severity"]) for f in findings)
        score = max(0, min(100, 100 - penalty))
        return score, findings[:80]

    def _static_checks(self, root: Path, files: list[Path]) -> list[dict]:
        findings: list[dict] = []
        readme = root / "README.md"
        dockerfile = root / "Dockerfile"
        env_example = root / ".env.example"

        if not readme.exists():
            findings.append(self._finding("documentation", "medium", "README.md", "README.md ausente.", "Adicione README com objetivo, instalação, arquitetura, endpoints e decisões técnicas."))
        if not dockerfile.exists():
            findings.append(self._finding("devops", "medium", "Dockerfile", "Dockerfile ausente.", "Adicione Dockerfile para padronizar ambiente e facilitar deploy."))
        if not env_example.exists():
            findings.append(self._finding("security", "low", ".env.example", "Arquivo .env.example ausente.", "Documente variáveis de ambiente sem expor segredos."))

        for file in files:
            relative = str(file.relative_to(root))
            content = safe_read(file)
            lower = content.lower()

            if len(content.splitlines()) > 450:
                findings.append(self._finding("architecture", "medium", relative, "Arquivo muito extenso.", "Divida responsabilidades em módulos menores para melhorar manutenção."))
            if "password" in lower and ("=" in content or ":" in content):
                findings.append(self._finding("security", "high", relative, "Possível credencial ou senha hardcoded.", "Use variáveis de ambiente ou secret manager."))
            if "todo" in lower or "fixme" in lower:
                findings.append(self._finding("quality", "low", relative, "Comentários TODO/FIXME encontrados.", "Transforme pendências em issues ou resolva antes de produção."))
            if "console.log" in content or "print(" in content:
                findings.append(self._finding("observability", "low", relative, "Logs simples encontrados.", "Use logger estruturado com níveis de severidade."))
            if "except:" in content:
                findings.append(self._finding("reliability", "medium", relative, "Tratamento genérico de exceção encontrado.", "Capture exceções específicas e registre contexto do erro."))

        return findings

    def _python_complexity(self, files: list[Path]) -> list[dict]:
        findings: list[dict] = []
        for file in [f for f in files if f.suffix == ".py"]:
            content = safe_read(file, 50000)
            try:
                blocks = cc_visit(content)
            except Exception:
                continue
            for block in blocks:
                if block.complexity >= 10:
                    findings.append(self._finding(
                        "complexity",
                        "high" if block.complexity >= 15 else "medium",
                        str(file.name),
                        f"Função/classe '{block.name}' com complexidade ciclomática {block.complexity}.",
                        "Refatore condicionais, extraia funções e reduza responsabilidades."
                    ))
        return findings

    def _bandit_scan(self, root: Path) -> list[dict]:
        findings: list[dict] = []
        try:
            result = subprocess.run(
                ["bandit", "-r", str(root), "-f", "json", "-q"],
                capture_output=True,
                text=True,
                timeout=25,
                check=False,
            )
            data = json.loads(result.stdout or "{}")
            for item in data.get("results", [])[:30]:
                findings.append(self._finding(
                    "security",
                    self._map_bandit(item.get("issue_severity", "LOW")),
                    item.get("filename"),
                    item.get("issue_text", "Possível vulnerabilidade encontrada."),
                    "Revise a vulnerabilidade apontada pelo scanner e aplique correção segura."
                ))
        except Exception:
            pass
        return findings

    def _map_bandit(self, severity: str) -> str:
        return {"HIGH": "critical", "MEDIUM": "high", "LOW": "medium"}.get(severity.upper(), "low")

    def _severity_penalty(self, severity: str) -> int:
        return {"critical": 15, "high": 9, "medium": 5, "low": 2}.get(severity, 1)

    def _finding(self, category: str, severity: str, file: str | None, message: str, recommendation: str) -> dict:
        return {"category": category, "severity": severity, "file": file, "message": message, "recommendation": recommendation}
