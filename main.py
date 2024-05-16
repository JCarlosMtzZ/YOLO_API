from fastapi import FastAPI
from router.file import file

app = FastAPI()

@app.get('/')
async def root():
    return {'message': "Root"}

app.include_router(file)