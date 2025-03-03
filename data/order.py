import json
from utils.utils import run_query
from query import order_query

async def create_order(
        order_id,
        user_id,
        item_ids,
        total_amount,
        status             
        ):
    params = [
        order_id,
        user_id,
        json.dumps(item_ids),
        total_amount,
        status
    ]
    return await run_query(query= order_query.CREATE_ORDER, params= params)

async def update_order_status(order_id: int, status):
    params = [
        status,
        str(order_id),
    ]
    return await run_query(query=order_query.UPDATE_ORDER_STATUS, params=params)
    

async def orders_list_by_status(status):
    params = [
        status
    ]
    return await run_query(query=order_query.FETCH_ORDER_BY_STATUS, params= params)

async def count_orders_status(status: str):
    params = [
        status
    ]
    return await run_query(query=order_query.COUNT_ORDER_BY_STATUS, params= params)

async def get_avg_processing_time():
    return await run_query(query=order_query.AVG_PROCESSING_TIME, params=[])
