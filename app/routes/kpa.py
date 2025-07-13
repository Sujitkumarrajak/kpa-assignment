# app/routes/kpa.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/kpa_form", tags=["KPA Form"])

# ✅ POST route
@router.post("/submit_kpa_form/", response_model=schemas.KPAFormOut)
async def submit_kpa_form(form: schemas.KPAFormCreate, db: AsyncSession = Depends(get_db)):
    new_form = models.KPAForm(**form.model_dump())
    db.add(new_form)
    await db.commit()
    await db.refresh(new_form)
    return new_form

# ✅ GET route
@router.get("/all_forms/", response_model=list[schemas.KPAFormOut])
async def get_all_forms(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.KPAForm))
    forms = result.scalars().all()
    return forms