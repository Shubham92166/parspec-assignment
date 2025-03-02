from queue import Queue
from data.order import update_order_status
from model.order import OrderStatus

order_queue = []

def add_order_to_queue(order_id: int):
    order_queue.put(order_id)
    update_order_status(order_id= order_id, status = OrderStatus.PROCESSING)
    return 
