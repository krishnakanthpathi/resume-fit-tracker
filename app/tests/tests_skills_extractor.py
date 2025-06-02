from app.services.skill_extractor import extract_skills

def test_extracts_expected_skills():
    text = "Experience with Docker, Python, and Flask"
    skills = extract_skills(text)
    assert "Python" in skills
    assert "Flask" in skills
    assert "Docker" in skills
    
