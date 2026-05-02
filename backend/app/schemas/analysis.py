from datetime import datetime
from pydantic import BaseModel, HttpUrl


class RepositoryAnalyzeRequest(BaseModel):
    repository_url: HttpUrl


class Finding(BaseModel):
    category: str
    severity: str
    file: str | None = None
    message: str
    recommendation: str


class AnalysisResponse(BaseModel):
    id: int
    repository_url: str | None
    project_name: str
    score: int
    summary: str
    findings: list[Finding]
    created_at: datetime

    class Config:
        from_attributes = True
