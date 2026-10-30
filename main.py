#27.10.2026
from app.crud.crud import (create_item, get_all_item, get_all_user, create_user,
    get_item_id, get_user_id, create_order, get_orders, update_order)
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas.schemas import OrderEditUpdate,ProductResponse, ProductCreate, UserCreate, OrderUpdate, OrderCreate, OrderResponse
from fastapi import Depends, FastAPI, HTTPException
from app.models.models import Order, User

app = FastAPI()

@app.post("/Items",response_model=ProductResponse)
def item_create (item:ProductCreate, db:Session = Depends(get_db)):
    return create_item(db, item)

@app.post("/Create_user",response_model=UserCreate)
def item_create (user:UserCreate, db:Session = Depends(get_db)):
    return create_user(db, user)

@app.get ("/Get_item_id", response_model=ProductResponse)
def get_item (id:int, db:Session = Depends(get_db)):
    db_item = get_item_id(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get ("/Get_user_id")
def get_user (id:int, db:Session = Depends(get_db)):
    db_user = get_user_id(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get ("/Get_all_user")
def users (db: Session = Depends(get_db)):
    return get_all_user(db)

@app.get ("/Get_all_items")
def items (db: Session = Depends(get_db)):
    return get_all_item(db)

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)  # SQLAlchemy 2.0: get по первичному ключу
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    db.delete(user)
    db.commit()

@app.get ("/Get_item_id", response_model=OrderResponse)
def get_item (id:int, db:Session = Depends(get_db)):
    db_item = get_item_id(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.post("/create_order", response_model=OrderResponse)
def cr_order(order: OrderCreate, db:Session = Depends(get_db)):
    return create_order(db, order)

@app.get ("/get_orders")
def orders (db: Session = Depends(get_db)):
    return get_orders(db)

@app.put("/order/{order_id}", response_model=OrderResponse)
def upd_item(order_id: int, data: OrderUpdate, db: Session = Depends(get_db)):
    return update_order(db, order_id, data)

@app.patch("/order/{order_id}", response_model=OrderResponse)
def edit_erder(order_id: int, data: OrderEditUpdate, db: Session = Depends(get_db)):
    return update_order(db, order_id, data)

@app.delete("/order/{order_id}", status_code=204)
def delete_user(order_id: int, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)  # SQLAlchemy 2.0: get по первичному ключу
    if not order:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    db.delete(order)
    db.commit()