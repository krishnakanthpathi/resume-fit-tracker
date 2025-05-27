import unittest
from app.skill_extractor import extract_skills

class TestSkillExtractor(unittest.TestCase):
    def test_extracts_expected_skills(self):
        text = "Experience with Docker, Python, and Flask"
        skills = extract_skills(text)
        self.assertIn("python", skills)
        self.assertIn("docker", skills)

if __name__ == "__main__":
    unittest.main()
