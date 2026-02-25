from pydantic import BaseModel
from pydantic import HttpUrl, Field
from typing import List, Optional


class Issue(BaseModel):
    type: str  
    description: str
    impact: str  
    element: Optional[str] = None

class AuditRequest(BaseModel):
    url: HttpUrl  

class AuditResponse(BaseModel):
    url: str
    score: int = Field(..., description="Accessibility score 0-100")   
    issues: List[Issue]



