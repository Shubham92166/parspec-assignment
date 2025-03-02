from queue import Queue
from data.order import update_order_status
from model.order import OrderStatus
import time
import uuid

order_queue = Queue()
order_list = []

def add_order_to_queue(order_id: int):
    order_queue.put(order_id)
    order_list.append(order_id)
    #await update_order_status(order_id= order_id, status = OrderStatus.PENDING)
    return {'status_code': 200}

async def process_orders_from_queue():
    while True:
        if not order_queue.empty():
            order_id = order_queue.get()
            await process_order(order_id, status = OrderStatus.PROCESSING.value)
            time.sleep(5)
            await process_order(order_id= order_id, status= OrderStatus.COMPLETED.value)
            print("Order processed succesfully")
    return True

async def process_order(order_id, status):
    return await update_order_status(order_id= order_id, status= status)

