from fastapi import FastAPI
from app.config import settings
from app.models import KnowledgeQuery, KnowledgeResponse
from app.services.rbac_kb import query_company_kb

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/ask", response_model=KnowledgeResponse)
def ask_kb(req: KnowledgeQuery):
    ans, granted, citation = query_company_kb(req.query, req.user_role)
    return KnowledgeResponse(query=req.query, answer=ans, access_granted=granted, citation=citation)
