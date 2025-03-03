from queue import Queue
from data.order import update_order_status
from model.order import OrderStatus

order_queue = Queue()
order_id_list = []

def add_order_to_queue(order_id: int):
    order_queue.put(order_id)
    order_id_list.append(order_id)
    return order_id_list

async def process_orders_from_queue():
    while True:
        if not order_queue.empty():
            order_id = order_queue.get()
            order_id_list.pop(0)
            await process_order(order_id, status = OrderStatus.PROCESSING.value)
            #await asyncio.sleep(10)
            await process_order(order_id= str(order_id), status= OrderStatus.COMPLETED.value)
            print("Order processed succesfully", order_id)
        else:
            break
    return True

async def process_order(order_id, status):
    return await update_order_status(order_id= order_id, status= status)

