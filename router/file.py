from fastapi import File, UploadFile, APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from config.db import get_db
import numpy as np
import json
import cv2

from schema.schemas import Item
from middleware.predictImage import predictImage

file = APIRouter(tags=['File'])

@file.post('/uploadfile/')
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):

    items_dict = {}
    items_objs = []
    items = []

    image_bytes = await file.read()
    image = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    items = predictImage(image)

    if items is None:
        raise HTTPException(status_code=500, detail="Prediction failed. Please try again later.")
    if len(items) <= 0:
        raise HTTPException(status_code=404, detail="No items found in the photo.")

    for item in items:
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1
    
    for name, quantity in items_dict.items():
        try:
            query = text('SELECT * FROM get_full_product(:name);')
            ext_item = db.execute(query, {'name': name}).fetchone()

            if not ext_item:
                continue

            curr_item = Item(
                code=ext_item[0],
                name=ext_item[1],
                quantity=quantity,
                unit_price=ext_item[2],
                discount_name=ext_item[3],
                discount_amount=ext_item[4]
            )
            items_objs.append(curr_item)
        
        except Exception as e:
            return {'message': f"Error processing product '{name}'. Please try again later."}

    if len(items_objs) <= 0:
        raise HTTPException(status_code=404, detail="No items found in database.")

    items_dicts = [item.to_dict() for item in items_objs]

    return items_dicts


@file.post('/predict/')
async def predict(file: UploadFile = File(...)):

    items_dict = {}
    items = []

    image_bytes = await file.read()
    image = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    items = predictImage(image)

    if items is None:
        raise HTTPException(status_code=500, detail="Prediction failed. Please try again later.")
    if len(items) <= 0:
        raise HTTPException(status_code=404, detail="No items found in the photo.")

    for item in items:
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1
    
    return json.dumps(items_dict)