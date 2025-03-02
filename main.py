from fastapi import FastAPI
from Controller import order, reporting
import threading
from helper.queue_handler import process_orders

app = FastAPI()

app.include_router(order.router, prefix='/order')
app.include_router(reporting.router, prefix='/reporting')

processing_thread = threading.Thread(target=process_orders)
processing_thread.daemon = True
processing_thread.start()
