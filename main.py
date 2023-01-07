from fastapi import FastAPI
import uvicorn
from app.routers import user
from app.db.database import engine, Base
from app.routers import user

# Create all tables in the database
def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI()
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
