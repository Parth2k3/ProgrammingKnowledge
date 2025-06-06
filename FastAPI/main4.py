postgres_uri = "postgresql://postgres.wgadcjwmtaaqlwcnmakd:6Vus3dH5LElqHqov@aws-0-ap-south-1.pooler.supabase.com:6543/postgres"
postgres_uri = "postgresql://postgres:6Vus3dH5LElqHqov@db.wgadcjwmtaaqlwcnmakd.supabase.co:5432/postgres"
postgres_uri = "postgresql://postgres.wgadcjwmtaaqlwcnmakd:6Vus3dH5LElqHqov@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"
from sqlmodel import SQLModel, Field
from typing import Optional

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False

from sqlmodel import create_engine, Session

engine = create_engine(postgres_uri, echo=True)

from fastapi import FastAPI
from contextlib import asynccontextmanager

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/items/")
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
from typing import List
from sqlmodel import select

@app.get("/items/", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
    