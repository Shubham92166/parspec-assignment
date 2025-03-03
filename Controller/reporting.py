from fastapi import APIRouter, HTTPException, status
from helper.queue_handler import order_id_list, order_queue
from Service import ReportingService as reporting_service

router = APIRouter()


@router.get('/get-queued-orders')
def get_all_queued_orders():
    try:
        queued_orders_id = order_id_list
        return {
                "status_code": status.HTTP_200_OK,
                "data": 
                {
                    "order id": queued_orders_id}
                }
    except (ModuleNotFoundError, ValueError) as e:
        print(e)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")
    
@router.get('/metrics')
async def get_all_metrics():
    try:
        response = await reporting_service.get_metrics()
        return {
            "data": response
        }
    except (ModuleNotFoundError, ValueError) as e:
        print(e)
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,detail= "Something went wrong!")
