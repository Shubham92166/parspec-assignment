from fastapi import APIRouter
from fastapi import Request
from model.order import OrderModel
from db_connection import get_db_connection
from Service import orderService as order_service

router = APIRouter()


@router.post('/create-order/')
async def create_order(
    input_data: OrderModel     
):
    order_data = input_data
    response = await order_service.create_order(order_data)
    return {
        "data" :  response
    }
            


                


        
