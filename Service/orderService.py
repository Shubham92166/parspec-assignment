from data import order as order_data
from model.order import OrderStatus
from utils.queue import add_order_to_queue
async def create_order(input_data: dict):
    input_data = input_data.dict()
    order_id = await order_data.create_order(
        input_data["user_id"],
        input_data["item_ids"],
        input_data["total_amount"],
        OrderStatus.PENDING)
    #push to queue
    if order_id != None:
        add_order_to_queue(order_id= order_id)
        return order_id
    else:
        return 500
    