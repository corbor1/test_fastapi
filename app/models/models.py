import uuid
from app.db.db import engine
from typing import Optional
from sqlalchemy import Float, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))

class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    price: Mapped[float] = mapped_column()
    count: Mapped[int] = mapped_column()

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    transactions: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)
    item_id: Mapped[int] = mapped_column()
    count: Mapped[int] = mapped_column()
    total_price: Mapped[float] = mapped_column()
    create_at:Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )