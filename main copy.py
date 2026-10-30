# uvicorn main:app --host 192.168.1.146 --port 8000
from app.db.db import get_db
from fastapi import FastAPI, HTTPException
from app.schemas.schemas import ProductCreate, ProductResponse

app = FastAPI()

db = {}

next_id = 1
def get_next_id() -> int:
    global next_id #1
    current = next_id #1
    next_id += 1# 2
    print (current)
    return current
    
@app.get("/")
def get_items():
    return [
        ProductResponse(id = id, name = data["name"], price = data["price"], count = data["count"])
        for id , data in db.items()
    ]

@app.get("/items/{item_id}",response_model= ProductResponse)
def get_item(id:int):
    item = db.get(id)
    if item is None:
        raise HTTPException (status_code=404, detail="Пользователь не найден")
    return ProductResponse(id = id, name=item["name"], price=item["price"], count=item["count"])

@app.post("/create_item",response_model=ProductCreate)
def create_item(item:ProductCreate):
    new_id = get_next_id()
    db[new_id] = {"name": item.name,
                  "price": item.price,
                  "count": item.count}
    return ProductCreate(name=item.name, price=item.price, count=item.count)

@app.put("/item/{item_id}",response_model=ProductResponse)
def item_update(id: int, item:ProductCreate):
    print (db)
    
    if id not in db:
        raise HTTPException(status_code=404,detail="Предмет не найден")
    db[id]["name"] = item.name
    db[id]["price"] = item.price
    db[id]["count"] = item.count

    return ProductResponse(
        id=id,
        name=db[id]["name"],
        price=db[id]["price"],
        count=db[id]["count"]
        )
@app.delete ("/delete/{item_id}", status_code= 204)
def delete_item (id:int):
    if id not in db:
        raise HTTPException(status_code=404, detail="Ошибка")
    del db[id]
    return "Удалили Данные"