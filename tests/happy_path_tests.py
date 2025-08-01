import pytest
from fastapi.testclient import TestClient
from main import app  # assuming your FastAPI app is in a file named main.py

client = TestClient(app)

def test_chat_endpoint_happy_path():
    # Create a new chat session first to get a session_id
    response = client.post("/sessions")
    assert response.status_code == 200
    session_data = response.json()
    session_id = session_data['session_id']

    # Test the chat endpoint with the new session_id
    chat_payload = {
        "query": "What is the capital of France?",
        "session_id": session_id
    }
    response = client.post("/chat", json=chat_payload)
    assert response.status_code == 200
    chat_response_data = response.json()
    assert 'response' in chat_response_data
    assert 'citations' in chat_response_data
    assert chat_response_data['session_id'] == session_id

def test_submit_feedback_happy_path():
    # Create a new chat session and interaction first to get interaction_id
    response = client.post("/sessions")
    assert response.status_code == 200
    session_data = response.json()
    session_id = session_data['session_id']

    # Create a chat interaction to get an interaction_id
    chat_payload = {
        "query": "What is the capital of France?",
        "session_id": session_id
    }
    response = client.post("/chat", json=chat_payload)
    assert response.status_code == 200
    interaction_data = response.json()
    interaction_id = interaction_data['interaction_id']

    # Test the feedback endpoint
    feedback_payload = {
        "interaction_id": interaction_id,
        "rating": 1,
        "feedback_text": "Great response!"
    }
    response = client.post("/feedback", json=feedback_payload)
    assert response.status_code == 200
    feedback_response_data = response.json()
    assert feedback_response_data['message'] == "Feedback submitted successfully"