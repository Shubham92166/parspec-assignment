import pymysql
from utils.db_connection import get_db_connection
from typing import Optional, Any, List, Dict

async def run_query(query: str, params: Optional[List[Any]] = None, fetchone: bool = False) -> Optional[Dict[str, Any]]:
    """
    Utility function to execute a SQL query.

    :param query: The SQL query to execute.
    :param params: A list of parameters to pass to the query (for parameterized queries).
    :param fetchone: If True, fetch a single record; otherwise, fetch all records.
    :return: The result of the query execution (either one row or all rows depending on fetchone).
    """
    connection = get_db_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                connection.commit()

                # Fetch results based on the fetchone flag
                if fetchone:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()

                return result
        except pymysql.MySQLError as e:
            print(f"Error executing query: {e}")
        finally:
            connection.close()

    return None
