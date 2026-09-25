from pydantic import BaseModel
from typing import List, Optional

class KnowledgeQuery(BaseModel):
    user_role: str  # 'intern', 'engineer', 'executive'
    query: str

class KnowledgeResponse(BaseModel):
    query: str
    answer: str
    access_granted: bool
    citation: Optional[str] = None
