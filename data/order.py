import json
from utils.query_executor import run_query
from query import order_query
async def create_order(
        user_id,
        item_ids,
        total_amount,
        status             
        ):
    params = [
        user_id,
        json.dumps(item_ids),
        total_amount,
        status
    ]
    await run_query(query= order_query.CREATE_ORDER, params= params)
    return await run_query(query= order_query.SELECT_LAST_INSERT, params=[])

async def update_order_status(order_id: int, status):
    params = [
        order_id,
        status
    ]
    await run_query(query=order_query.UPDATE_ORDER_STATUS, params=params)
