import time
from fastapi.testclient import TestClient
from src.main import app
import pytest
from tests.exports.variables import ACCESS_TOKEN


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_data_websocket_server(client):
    # Connect to the WebSocket endpoint
    with client.websocket_connect(f"/wearable/ws/{ACCESS_TOKEN}") as websocket:
        # Send a JSON message after connecting
        while True:
            websocket.send_json(
                {
                    "glucoseLevel": 150,
                    "heartRate": 80,
                    "bloodPressure": 120,
                    "temperature": 98.6,
                }
            )

            # Receive and check for push notification
            data = websocket.receive_json()
            if data == "You are connected to the server":
                break


def test_data_websocket_glucose(client):
    # Connect to the WebSocket endpoint
    with client.websocket_connect(f"/wearable/ws/{ACCESS_TOKEN}") as websocket:
        # Send a JSON message after connecting
        while True:
            websocket.send_json(
                {
                    "glucoseLevel": 150,
                    "heartRate": 80,
                    "bloodPressure": 120,
                    "temperature": 96.6,
                }
            )

            # Receive and check for push notification
            data = websocket.receive_json()
            if (
                data
                == "Hey your current glucose level: 150 is unusual. Please take care."
            ):
                break


def test_data_websocket_heart_rate(client):
    # Connect to the WebSocket endpoint
    with client.websocket_connect(f"/wearable/ws/{ACCESS_TOKEN}") as websocket:
        # Send a JSON message after connecting
        while True:
            websocket.send_json(
                {
                    "glucoseLevel": 150,
                    "heartRate": 110,
                    "bloodPressure": 120,
                    "temperature": 96.6,
                }
            )

            # Receive and check for push notification
            data = websocket.receive_json()
            if (
                data
                == "Hey your current heart rate level: 110 is unusual. Please take care."
            ):
                break


def test_data_websocket_blood_pressure(client):
    # Connect to the WebSocket endpoint
    with client.websocket_connect(f"/wearable/ws/{ACCESS_TOKEN}") as websocket:
        # Send a JSON message after connecting
        while True:
            websocket.send_json(
                {
                    "glucoseLevel": 150,
                    "heartRate": 80,
                    "bloodPressure": 166,
                    "temperature": 96.6,
                }
            )

            # Receive and check for push notification
            data = websocket.receive_json()
            if (
                data
                == "Hey your current blood pressure level: 166 is unusual. Please take care."
            ):
                break


def test_data_websocket_temperature(client):
    # Connect to the WebSocket endpoint
    with client.websocket_connect(f"/wearable/ws/{ACCESS_TOKEN}") as websocket:
        # Send a JSON message after connecting
        while True:
            websocket.send_json(
                {
                    "glucoseLevel": 150,
                    "heartRate": 80,
                    "bloodPressure": 120,
                    "temperature": 96,
                }
            )

            # Receive and check for push notification
            data = websocket.receive_json()
            if (
                data
                == "Hey your current temperature level: 96 is unusual. Please take care."
            ):
                break
