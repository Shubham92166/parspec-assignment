CREATE_ORDER = "INSERT INTO orders (user_id, item_ids, total_amount, status) VALUES (%s, %s, %s, %s);"
SELECT_LAST_INSERT = "SELECT LAST_INSERT_ID();"
UPDATE_ORDER_STATUS = "UPDATE TABLE orders set status = '%s', updated_at = now() where order id = %s";
