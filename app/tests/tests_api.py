from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_evaluate_fit():
    payload = {
        "resume_text": "Experience in Python and Flask.",
        "job_description": "Looking for Python and Flask developers with Docker experience."
    }
    response = client.post("/evaluate-fit", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "fit_score" in json_data
    assert "missing_skills" in json_data
    assert "matched_skills" in json_data
    assert "recommended_learning_track" in json_data
    assert "verdict" in json_data
    assert "status" in json_data
    assert json_data["status"] == "ok"
