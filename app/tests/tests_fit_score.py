import unittest
from app.services.fit_score_engine import fit_score_calculater
from pydantic import BaseModel

class DummyRequest(BaseModel):
    resume_text: str
    job_description: str

class TestFitScore(unittest.TestCase):
    def test_similarity_score_output(self):
        req = DummyRequest(
            resume_text="Experience in Python, Flask, and SQL.",
            job_description="Looking for a backend developer with Python and SQL."
        )
        score = fit_score_calculater(req)
        self.assertIsInstance(score, float)
        self.assertGreater(score, 0.0)
        self.assertLessEqual(score, 1.0)

if __name__ == "__main__":
    unittest.main()
