from fastapi import FastAPI
from config import settings

app = FastAPI()
print(settings.database_url)
@app.get("/")
def read_root():
    return {
        "db_url": settings.database_url,
        "secret_key": settings.secret_key
    }
