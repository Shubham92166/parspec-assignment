from data import order as order_data
from model.order import OrderStatus
from helper.queue_handler import add_order_to_queue
import asyncio
from fastapi import HTTPException
from utils.utils import generate_order_id

async def create_order(input_data: dict):
    try:
        input_data = input_data.dict()
        order_id = generate_order_id()
        await order_data.create_order(
            order_id,
            input_data["user_id"],
            input_data["item_ids"],
            input_data["total_amount"],
            OrderStatus.PENDING.value)
        #push to queue
        add_order_to_queue(order_id=order_id)
        return {"order_id": order_id}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Something went wrong!")
    
async def fetch_orders_by_status(status: OrderStatus):
    return await order_data.orders_list_by_status(status)
    
async def count_orders_by_status(status: OrderStatus):
    return await order_data.count_orders_status(status)

async def get_metrics():
    order_statuses = ["PENDING", "PROCESSING", "COMPLETED"]
    results = await asyncio.gather(
        *[count_orders_by_status(status) for status in order_statuses]
    )

    try:
        pending_orders, processing_orders, completed_orders = results
        total_processed_orders = completed_orders #total count processed orders

        avg_processing_time_in_seconds = await order_data.get_avg_processing_time()

        if avg_processing_time_in_seconds == None:
            return "No data to show metrics!!"
        else:
            return {
                "Pending orders:", pending_orders,
                "COmpleted orders:", completed_orders,
                "Processing orders:", processing_orders,
                "Average processing time:", avg_processing_time_in_seconds
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    



    
