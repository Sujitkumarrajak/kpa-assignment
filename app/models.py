from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.database import Base

class KPAForm(Base):
    __tablename__ = "kpa_forms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    kpa_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())