
from fastapi import FastAPI
from rotas import rota



app = FastAPI()

app.include_router(rota, prefix='')




# uvicorn main:app --reload