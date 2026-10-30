import datetime
from typing import Optional
import uuid
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    
class ProductCreate(BaseModel):
    name: str
    price: float
    count: int

class ProductResponse(ProductCreate):
    id: int

class OrderCreate(BaseModel):
    user_id: int
    item_id: int
    count: int
    total_price: float
    
class OrderUpdate(BaseModel):
    user_id: int
    item_id: int
    count: int
    total_price:float

class OrderResponse(OrderUpdate):
    id: int
    transactions: uuid.UUID

class OrderEditUpdate(BaseModel):
    user_id: Optional[int] = None
    item_id: Optional[int] = None
    count: Optional[int] = None
    total_price:Optional[float] = None