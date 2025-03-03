from fastapi import APIRouter, HTTPException, status
from helper.queue_handler import order_id_list, order_queue
from Service import ReportingService as reporting_service

router = APIRouter()


@router.get('/get-queued-orders')
def get_all_queued_orders():
    """
    Retrieves all queued orders.

    This endpoint returns the list of order IDs that are currently in the queue. 
    The order IDs are fetched from a predefined list (`order_id_list`).

    Returns:
        dict: A dictionary containing a status code and the list of queued order IDs. 
              The key "data" contains the queued order IDs under the "order id" key.

    Raises:
        HTTPException: If an error occurs during the fetching of the queued orders, 
                        a 500 Internal Server Error will be raised with the message 
                        "Something went wrong!".

    Example:
        GET /get-queued-orders
        {
            "status_code": 200,
            "data": {
                "order id": [1234, 5678, 91011]
            }
        }
    """
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
    """
    Fetches and returns all available metrics.

    This endpoint retrieves various metrics related to the system or application.
    The exact nature of the metrics depends on the implementation in the `reporting_service`.

    Returns:
        dict: A dictionary containing the metrics. The key "data" contains the list of metrics.

    Raises:
        HTTPException: If an error occurs during the fetching of the metrics, a 500 Internal 
                        Server Error will be raised with the message "Something went wrong!".

    Example:
        GET /metrics
        {
            "data": [
                {"metric_name": "order_count", "value": 123},
                {"metric_name": "avg_processing_time", "value": 5.6},
                ...
            ]
        }
    """
    try:
        response = await reporting_service.get_metrics()
        return {
            "data": response
        }
    except (ModuleNotFoundError, ValueError) as e:
        print(e)
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,detail= "Something went wrong!")
