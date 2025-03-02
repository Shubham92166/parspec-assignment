CREATE_ORDER = "INSERT INTO orders (order_id, user_id, item_ids, total_amount, status) VALUES (%s, %s, %s, %s, %s);"
UPDATE_ORDER_STATUS = "UPDATE TABLE orders set status = '%s', updated_at = now() where order id = %s";
COUNT_ORDER_BY_STATUS = "select count(order_id) from orders where status = {status}";
FETCH_ORDER_BY_STATUS = "select * from orders where status = {status}";
AVG_PROCESSING_TIME = """
                    SELECT AVG(TIMESTAMPDIFF(SECOND, created_at, updated_at)) AS avg_processing_time_second
               `    FROM orders
                    WHERE status = 'COMPLETED'
                    """