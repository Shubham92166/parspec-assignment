Overview:
This project is a FastAPI-based application that allows you to manage and process orders. It provides an API with endpoints to create orders, view orders by status, and track the processing time of orders(metrics).

Features:
Create Orders: Create a new order with the provided user details and items, push it to in-memory queue and process orders asynchronously.
Get Orders by Status: Fetch orders based on their status (Pending, Processing, Completed).
Metrics: Calculate and return the average processing time of all processed orders, total orders processed, total orders completed, total pending orders.

Technologies Used:

FastAPI: For creating the web API.

Uvicorn: ASGI server for running the FastAPI application.

Pydantic: For data validation and serialization.

MySQL: For storing data in database.

pytest: For unit testing the application.

Setup:
1. Prerequisites:
    Python 3.8+
    pip (Python package installer)

2. Installation Steps
    1. Clone the repository:
    git clone https://github.com/Shubham92166/parspec-assignment.git

    cd parspec_assignment

    3. Create and activate a virtual environment:
   
    On Windows:
    python -m venv venv
    .\venv\Scripts\activate

   On macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

3. Install the required dependencies:
    pip install -r requirements.txt

4. Running the Application
    Once the dependencies are installed, you can run the FastAPI app using Uvicorn:
    uvicorn app.main:app --reload

    This will start the FastAPI application, and it will be accessible at http://127.0.0.1:8000. To take advantage of FastAPI’s asynchronous nature, avoid blocking operations in the event loop. You can also access the interactive Swagger UI documentation for your API by going to:

    http://127.0.0.1:8000/docs


API Endpoints:
    POST order/create-order
    Create a new order asynchronously.
    
Request Body:
        
            {
            "user_id": 1,
            "item_ids": [1, 2],
            "total_amount": 100.0
            }
    
Response body:
    
            {
            "status": 201,
            "data": {
                "order_id": "5eea1442-4b39-453a-8dff-04f658754eaf"
            }

GET order/status/{status_name}
    
Get orders by status asynchronously.

Request Body:

URL Parameters:
1. status_name (required): The status of the order (e.g., "pending", "processing", "completed").

        Response Body:

        [
            {
                "order_id": "876aeac7-d30a-42b6-9262-8ed4cfb8a1d2",
                "user_id": 3,
                "items_id": "[4, 6]",
                "total_amount": 220099.0,
                "created_at": "COMPLETED",
                "updated_at": "2025-03-03T08:54:00"
            },
            {
                "order_id": "5ce460e1-dfc5-4e5e-8fe8-6fb7e3fe11ee",
                "user_id": 3,
                "items_id": "[4, 6]",
                "total_amount": 220099.0,
                "created_at": "COMPLETED",
                "updated_at": "2025-03-03T08:57:09"
            },
            {
                "order_id": "c8543d98-5712-4bf8-a0bf-bc0b51e93195",
                "user_id": 3,
                "items_id": "[4, 6]",
                "total_amount": 220099.0,
                "created_at": "COMPLETED",
                "updated_at": "2025-03-03T09:00:22"
            },
            {
                "order_id": "cb144fa9-3845-4dd5-aac9-017c545eb3e3",
                "user_id": 3,
                "items_id": "[4, 6]",
                "total_amount": 220099.0,
                "created_at": "COMPLETED",
                "updated_at": "2025-03-03T10:55:47"
            },
            {
                "order_id": "983e09da-c97e-465d-9806-ae519cfd589e",
                "user_id": 3,
                "items_id": "[4, 6]",
                "total_amount": 220099.0,
                "created_at": "COMPLETED",
                "updated_at": "2025-03-03T10:56:36"
            },
            {
                "order_id": "c696ea71-7cbf-4795-bc4d-95d99754835e",
                "user_id": 3,
                "items_id": "[4, 6]",
                "total_amount": 220099.0,
                "created_at": "COMPLETED",
                "updated_at": "2025-03-03T10:56:39"
            },
            {
                "order_id": "46a4d2a1-56f9-4e43-9d24-9199e8388f9d",
                "user_id": 3,
                "items_id": "[4, 6]",
                "total_amount": 220099.0,
                "created_at": "COMPLETED",
                "updated_at": "2025-03-03T10:56:42"
            },
            {
                "order_id": "5eea1442-4b39-453a-8dff-04f658754eaf",
                "user_id": 3,
                "items_id": "[4, 6]",
                "total_amount": 220099.0,
                "created_at": "COMPLETED",
                "updated_at": "2025-03-03T12:14:28"
            }
        ]

GET /metrics
    Get the order related metrics asynchronously.

Response Body:

    {
    "data": {
        "Total orders processed": 8,
        "Pending orders:": 11,
        "Completed orders:": 8,
        "Processing orders:": 0,
        "Average processing time:": 2.875
        }
    }

Design Decisions:


1. FastAPI Web Framework: Since we are working on Asynchronous order processing then we need to use such a framework which could support asnyc without compromising the performance of the application. In such case, FastAPI is a better choice as it supports async calls and it doesn't affect the system performance. It can scale and handle large number of requests concurrently improving the overall effective utitlisation of resources.

2. MySQL Database: in Ecom applications, mostly the data remains structured so we need a database which stores data in structured fashion. Thus, MySQL or PostgreSQL are better choice. If load increases then we can migrate to PostgreSQL as it can scale better compared to MySQL.

3. Creating order_id in the code itself instead of using db auto increment as while scaling this would create problem because two db instance might generate same order_id as it is just auto incremented value and this would create conflict because two orders cannot have same order_id. So, there should be a central logic to create a unique order_id. For now, I am also storing it in db for any future use case.

    Database schema:
    Orders table creation

        CREATE TABLE orders (
        order_id VARCHAR(50) NOT NULL,
        user_id INT NOT NULL,
        item_ids JSON NOT NULL,
        total_amount FLOAT NOT NULL,
        status ENUM('PENDING', 'PROCESSING', 'COMPLETED') DEFAULT 'PENDING',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (order_id)
        );

Assumtions made during development:
1. The Ecom application will have structured data
2. System should be reliable and available and performance will be a concern
3. API requests per second will be around 1,000  


