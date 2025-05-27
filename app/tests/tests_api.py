import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPI(unittest.TestCase):
    def test_health_endpoint(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_evaluate_fit(self):
        payload = {
            "resume_text": "Experience in Python and Flask.",
            "job_description": "Looking for Python and Flask developers with Docker experience."
        }
        response = client.post("/evaluate-fit", json=payload)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn("fit_score", json_data)
        self.assertIn("missing_skills", json_data)

if __name__ == "__main__":
    unittest.main()
