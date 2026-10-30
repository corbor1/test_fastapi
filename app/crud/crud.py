import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.models import Item, User, Order
from app.schemas.schemas import ProductCreate, UserCreate, OrderCreate, OrderUpdate

def create_item(db:Session, item: ProductCreate):
    # db_item = Item(**item.model_dump())# Вот тут разобраться я так понимаю мне тут нужно сделать проверку по значениям
    db_item = Item(
        name = item.name,
        price = item.price,
        count = item.count,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_user (db:Session, user:UserCreate):
    db_user= User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_id(db:Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_item_id(db:Session, id: int):
    return db.query(Item).filter(Item.id == id).first()

def get_all_item(db:Session):
    return db.query(Item).all()

def get_all_user(db:Session):
    return db.query(User).all()

def create_order(db: Session, data: OrderCreate):
    order = Order(
        user_id=data.user_id,
        item_id=data.item_id,
        count=data.count,
        total_price=data.total_price,
        transactions=uuid.uuid4(),  # питоновский UUID, гарантированно не None
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders(db:Session):
    return db.query(Order).all()

def update_order(db: Session, order_id: int, data: OrderUpdate):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")

    # Частичное обновление: меняем только переданные поля
    if data.user_id is not None:
        order.user_id = data.user_id
    if data.item_id is not None:
        order.item_id = data.item_id
    if data.count is not None:
        order.count = data.count
    if data.total_price is not None:
        order.total_price = data.total_price

    db.commit()
    db.refresh(order)
    return order