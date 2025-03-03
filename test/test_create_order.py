# from fastapi import HTTPException
# from fastapi.testclient import TestClient
import pytest
# from unittest import mock
# import asyncio
# import os
# print(os.getcwd())  # Print the current working directory

#from Controller.order import create_order
from ..Service import OrderService
#from helper.queue_handler import process_order, process_orders_from_queue
#from model.order import OrderModel


#from main import app


# @pytest.fixture
# def client():
#     # This fixture creates a TestClient for sending HTTP requests to the FastAPI app
#     return TestClient(app)


# def test_create_order_controller_success(client):
#     # Arrange: Mock request data
#     order_data = {
#         "user_id": 1,
#         "item_ids": [101, 102],
#         "total_amount": 250.5
#     }

#     # Mock the service layer function
#     with mock.patch("Service.OrderService.create_order") as mock_create_order:

#         # Simulate successful order creation
#         mock_create_order.return_value = {"order_id": "order_123"}

#         # Act: Send a POST request to the API endpoint
#         response = client.post("/create-order/", json=order_data)

#         # Assert: Check if the response is correct
#         assert response.status_code == 201
#         assert response.json() == {"status": 201, "data": {"order_id": "order_123"}}

#         # Ensure that the service layer was called with the correct arguments
#         mock_create_order.assert_called_once_with(order_data)
