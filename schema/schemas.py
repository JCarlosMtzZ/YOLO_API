from pydantic import BaseModel
from datetime import datetime

class Product_schema(BaseModel):
    id: int
    code: str
    name: str
    unitprice: float

class Discount_schema(BaseModel):
    id: int
    name: str
    amount: float
    startdate: datetime
    enddate: datetime