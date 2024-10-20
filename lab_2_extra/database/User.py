import uuid
from sqlalchemy import UUID, Column, String, Integer
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(AsyncAttrs, DeclarativeBase):
    __mapper_args__ = {"eager_defaults": True}


class User(Base, AsyncAttrs):
    __tablename__ = 'users'
    id: Mapped[UUID] = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                              default=uuid.uuid4)
    name: Mapped[str] = Column(String(50), nullable=False)
    age: Mapped[int] = Column(Integer, nullable=True)
