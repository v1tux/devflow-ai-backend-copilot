from app.core.config import get_settings

settings = get_settings()


class AIService:
    def generate_summary(self, project_name: str, findings: list[dict], score: int) -> str:
        # Fallback local para funcionar mesmo sem chave da OpenAI.
        critical = len([f for f in findings if f.get("severity") == "critical"])
        high = len([f for f in findings if f.get("severity") == "high"])
        medium = len([f for f in findings if f.get("severity") == "medium"])

        if score >= 85:
            level = "excelente"
        elif score >= 70:
            level = "boa"
        elif score >= 50:
            level = "intermediária"
        else:
            level = "crítica"

        return (
            f"O projeto {project_name} recebeu score {score}/100 e apresenta qualidade {level}. "
            f"Foram encontrados {critical} pontos críticos, {high} altos e {medium} médios. "
            "Priorize segurança, redução de complexidade, padronização arquitetural e melhoria da documentação técnica."
        )
