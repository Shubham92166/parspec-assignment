from fastapi import APIRouter, HTTPException, status
from helper.queue_handler import order_list, order_queue

router = APIRouter()


@router.get('/get-queued-orders')
def get_all_queued_orders():
    try:
        queued_orders_id = order_list
        return {
                "status_code": status.HTTP_200_OK,
                "data": 
                {
                    "order id": queued_orders_id}
                }
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")