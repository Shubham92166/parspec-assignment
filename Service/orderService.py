from data import order as order_data
from model.order import OrderStatus
from helper.queue_handler import add_order_to_queue
from fastapi import HTTPException, status
from utils.utils import generate_order_id
from helper.queue_handler import process_orders_from_queue

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
        #background_tasks.add_task(process_orders_from_queue)
        response = await process_orders_from_queue()
        return {"order_id": order_id}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Something went wrong!")
    
async def fetch_all_orders_by_status(status: OrderStatus):
    result = await order_data.orders_list_by_status(status)
    response = []
    for res in result:
        response.append(
           { "order_id": res[0],
            "user_id": res[1],
            "items_id": res[2],
            "total_amount": res[3],
            "created_at": res[4],
            "updated_at": res[5]
           }
        )
    return response

async def count_orders_by_status(status: OrderStatus):
    return await order_data.count_orders_status(status)