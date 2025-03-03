import asyncio
from fastapi import FastAPI
from Controller import order, reporting

app = FastAPI()

app.include_router(order.router, prefix='/order')
app.include_router(reporting.router, prefix='/reporting')
