import asyncio
import uvicorn
from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.User import User
from database.init_database import get_session
from database.init_database import init_database

rt = APIRouter(prefix='/api')


@rt.get('/reg_user')
async def registration_user(
        name: str,
        age: int,
        session: AsyncSession = Depends(get_session)
):
    new_user = User(name=name, age=age)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return {'instance': new_user}


@rt.get('/get_users')
async def get_users_by_name(
        name: str,
        session: AsyncSession = Depends(get_session)
):
    users = await session.execute(select(User).filter_by(name=name))
    return {'users': users.scalars().all()}


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin", "Authorization"],
)

app.include_router(rt)


async def main():
    await init_database()


if __name__ == '__main__':
    asyncio.run(main())
    uvicorn.run(app, host='0.0.0.0', port=8000)
