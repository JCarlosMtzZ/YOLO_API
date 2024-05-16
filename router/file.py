from fastapi import File, UploadFile, APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from config.db import get_db
import requests

import random

from config.function import CLASSIFICATION_URL

fruit_names = [
    'Apple', 'Banana', 'Orange', 'Grape', 'Strawberry', 'Watermelon',
    'Pineapple', 'Kiwi', 'Mango', 'Peach', 'Pear', 'Plum', 'Cherry',
    'Blueberry', 'Raspberry', 'Lemon', 'Lime', 'Grapefruit', 'Pomegranate',
    'Cantaloupe', 'Melon'
]

def get_image_details():
    num = random.randint(1, 10)
    fruits = []
    for i in range(num):
        fruit_num = random.randint(0, len(fruit_names)-1)
        fruits.append(fruit_names[fruit_num])
    return fruits

class Item:
    def __init__(self, code, name, quantity, unit_price,
                 discount_name, discount_amount):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.discount_name = discount_name
        self.discount_amount = discount_amount
    
    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'quantity': str(self.quantity),
            'unit_price': str(self.unit_price),
            'discount_name': self.discount_name,
            'discounnt_amount': str(self.discount_amount)
        }

file = APIRouter(tags=['File'])

@file.post('/uploadfile/')
async def upload_file(file: UploadFile = File(...),
                      db: Session = Depends(get_db)):

    items_dict = {}
    items_objs = []

    #with requests.post(CLASSIFICATION_URL, files={"file": (file.filename, file.file)}) as response:
        #if response.status_code == 200:
            #json_response = response.json()

    json_response = get_image_details()

    for item in json_response:
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1
    
    for name, quantity in items_dict.items():
        query = text('SELECT * FROM get_full_product(:name);')
        ext_item = db.execute(query, {'name': name}).fetchone()
        curr_item = Item(
            code=ext_item[1],
            name=ext_item[2],
            quantity=quantity,
            unit_price=ext_item[3],
            discount_name=ext_item[4],
            discount_amount=ext_item[5]
        )
        items_objs.append(curr_item)
    items_dicts = [item.to_dict() for item in items_objs]
    return items_dicts

    #else:
    #    return JSONResponse(content=response.status_code)