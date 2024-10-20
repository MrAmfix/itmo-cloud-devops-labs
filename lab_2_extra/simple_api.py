from fastapi import FastAPI, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.User import Base, User
from database.utils import engine, get_session


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/api/reg_user")
async def register_user(name: str, age: int, db: AsyncSession = Depends(get_session)):
    new_user = User(name=name, age=age)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {"message": "User registered successfully", "User": {"id": new_user.id, "name": name, "age": age}}


@app.get("/api/get_users")
async def get_users(name: str, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(User).where(User.name == name))
    users = result.scalars().all()
    return {"users": [{"id": user.id, "name": user.name, "age": user.age} for user in users]}
