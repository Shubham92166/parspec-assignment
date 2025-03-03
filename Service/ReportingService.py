import asyncio
from data import order as order_data
from fastapi import HTTPException, status
from Service.OrderService import count_orders_by_status

async def get_metrics():
    order_statuses = ["PENDING", "PROCESSING", "COMPLETED"]
    results = await asyncio.gather(
        *[count_orders_by_status(status) for status in order_statuses]
    )

    try:
        pending_orders, processing_orders, completed_orders = results
        total_processed_orders = completed_orders #total count processed orders

        avg_processing_time_in_seconds = await order_data.get_avg_processing_time()

        if avg_processing_time_in_seconds == None:
            return "No data to show metrics!!"
        else:
            return {
                "Total orders processed": total_processed_orders[0][0],
                "Pending orders:": pending_orders[0][0],
                "Completed orders:": completed_orders[0][0],
                "Processing orders:": processing_orders[0][0],
                "Average processing time:": avg_processing_time_in_seconds[0][0]
            }
    except (ModuleNotFoundError, ValueError) as e:
        print(e)
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error: {str(e)}")
