# main.py
from fastapi import FastAPI
from Controller.order import router
import threading
#from queue_handler import process_orders

app = FastAPI()

# Include the order router
app.include_router(router)

# Start the order processing thread
# processing_thread = threading.Thread(target=process_orders)
# processing_thread.daemon = True
# processing_thread.start()
