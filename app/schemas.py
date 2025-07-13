from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 👉 Request model (what you receive in POST)
class KPAFormCreate(BaseModel):
    name: str
    department: str
    kpa_text: str

# 👉 Response model (what you return from DB)
class KPAFormOut(KPAFormCreate):
    id: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True  # ✅ Works for Pydantic v2+; use `orm_mode = True` if using v1