import shutil
import tempfile
from pathlib import Path
from git import Repo


class RepositoryService:
    def clone(self, repository_url: str) -> Path:
        temp_dir = Path(tempfile.mkdtemp(prefix="devflow_repo_"))
        try:
            Repo.clone_from(repository_url, temp_dir, depth=1)
            return temp_dir
        except Exception as exc:
            shutil.rmtree(temp_dir, ignore_errors=True)
            raise ValueError("Não foi possível clonar o repositório. Verifique se a URL é pública e válida.") from exc

    def cleanup(self, path: Path) -> None:
        shutil.rmtree(path, ignore_errors=True)
