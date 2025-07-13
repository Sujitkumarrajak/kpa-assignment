# KPA Assignment API

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- Alembic
- Python-dotenv

## Setup
1. Create virtualenv & activate
2. Install requirements.txt
3. Configure .env file (DATABASE_URL)
4. Run server: uvicorn app.main:app --reload

## API Implemented
- POST /kpa_form/submit_kpa_form/
- GET /kpa_form/all_forms/

## Notes
- Validated using Pydantic
- Connected to PostgreSQL
- Tested using Postman and Swagger UI
