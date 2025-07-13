from fastapi import FastAPI
from app.routes import kpa
from app.database import engine, Base
from app.routes.kpa import router as kpa_router

app = FastAPI()

app.include_router(kpa_router) 

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)