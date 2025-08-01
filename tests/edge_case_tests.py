from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_non_existent_document():
    # Attempt to get a citation for a chunk with a non-existent ID
    response = client.get("/citations/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Citation not found"}

def test_read_non_existent_chat_history():
    # Attempt to get the history of a non-existent session
    response = client.get("/sessions/999/history")
    assert response.status_code == 404
    assert response.json() == {"detail": "Session not found"}