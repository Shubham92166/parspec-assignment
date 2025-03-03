from fastapi import APIRouter, HTTPException, status
from model.order import OrderModel, OrderStatus
from Service import OrderService as order_service
from pydantic import ValidationError

router = APIRouter()


@router.post('/create-order/')
async def create_order(
    input_data: OrderModel
):
    """
    Create a new order in the system.

    This endpoint accepts an order object (OrderModel), processes it, and returns a 
    response with the order's creation status and the created order data.

    Args:
        input_data (OrderModel): The order data containing user ID, item IDs, and total amount.

    Returns:
        dict: A dictionary containing:
            - "status" (int): The HTTP status code indicating the result of the order creation (e.g., 201 for created).
            - "data" (dict): The response from the service layer containing the order details.

    Raises:
        HTTPException: If an error occurs during the order creation process, a 500 Internal Server Error is raised with a detailed error message.
    """
    try:
        order_data = input_data
        response = await order_service.create_order(order_data)
        return {
            "status": status.HTTP_201_CREATED,
            "data" :  response
        }
    except (ModuleNotFoundError, ValueError) as e:
        print(e)
        return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")

@router.get("/status/{status_name}/")
async def get_orders_by_status(status_name):
    """
    Fetches all orders by their status.

    This endpoint retrieves all orders that match the provided order status. The 
    `status_name` parameter should be a valid order status (e.g., "PENDING", "COMPLETED").

    Args:
        status_name (str): The status of the orders to fetch. It is expected to be one of 
                            the predefined order statuses, which will be converted to uppercase 
                            before querying.

    Returns:
        dict: A dictionary containing the orders that match the provided status. The key 
              "data" contains a list of orders that match the status.

    Raises:
        HTTPException: If an error occurs during the process, a 500 Internal Server Error 
                        will be raised with the message "Something went wrong!".

    Example:
        GET /status/completed/
        {
            "data": [
                {"order_id": "1", "status": "COMPLETED", ...},
                {"order_id": "2", "status": "COMPLETED", ...}
            ]
        }
    """
    try:
        order_status = status_name.upper()
        response = await order_service.fetch_all_orders_by_status(order_status)
        return {
            "data": response
        }
    except (ModuleNotFoundError, ValueError) as http_exc:
        print(http_exc)
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Something went wrong!")
        




    






                


        
