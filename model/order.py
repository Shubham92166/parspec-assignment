import enum
from typing import List
from pydantic import BaseModel
class OrderModel(BaseModel):
    user_id: int
    item_ids: List[int]
    total_amount: float
    status: str

class OrderStatus(enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"



