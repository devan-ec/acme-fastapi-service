from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="acme-fastapi-service", openapi_url=None)


class ReportRequest(BaseModel):
    title: str = Field(min_length=1)
    tags: list[str] = []


class Report(BaseModel):
    report_id: str
    title: str
    tags: list[str]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/reports/{report_id}", response_model=Report)
def get_report(report_id: str) -> Report:
    return Report(report_id=report_id, title="Weekly summary", tags=[])


@app.get("/reports", response_model=list[Report])
def list_reports(tag: str | None = None) -> list[Report]:
    return []


@app.post("/reports", response_model=Report, status_code=201)
def create_report(body: ReportRequest) -> Report:
    return Report(report_id="RPT-0001", title=body.title, tags=body.tags)
