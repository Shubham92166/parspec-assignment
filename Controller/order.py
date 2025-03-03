from fastapi import APIRouter, HTTPException, status
from model.order import OrderModel, OrderStatus
from Service import OrderService as order_service

router = APIRouter()


@router.post('/create-order/')
async def create_order(
    input_data: OrderModel
):
    try:
        order_data = input_data
        response = await order_service.create_order(order_data)
        return {
            "status": status.HTTP_201_CREATED,
            "data" :  response
        }
    except (ModuleNotFoundError, ValueError) as e:
        print(e)
        return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something wen wrong!")

@router.get("/status/{status_name}/")
async def get_orders_by_status(status_name: str):
    try:
        order_status = status_name.upper()
        response = await order_service.fetch_all_orders_by_status(order_status)
        print(response)
        if not response:    
            raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Something went wrong!")
        return response
        
    except (ModuleNotFoundError, ValueError) as http_exc:
        print(http_exc)
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Something went wrong!")
        




    






                


        
