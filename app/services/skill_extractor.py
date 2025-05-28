from pandas import read_csv

from app.utils.text_cleaner import clean_text

from app.models.request_models import evaluate_fit_request

try:
    df = read_csv('app/data/skills_dataset.csv', names=['skills'])
    skills = df['skills']
except Exception as e:
    print(f"Error loading skills dataset: {e}")
    skills = []

def extract_skills(text: str) -> set:
    try:
        text = clean_text(text)
        text = set(text.split())  # Convert to set for faster lookup
        found_skills = set()
        for skill in skills:
            if skill.lower() in text:
                found_skills.add(skill.lower())
        return found_skills
    except Exception as e:
        print(f"Error extracting skills: {e}")
        return set()

def extract_missing_skills(req: evaluate_fit_request) -> list:
    try:
        resume_text: str = req.resume_text
        job_description: str = req.job_description

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        missing_skills = job_skills - resume_skills

        return list(missing_skills)
    except Exception as e:
        print(f"Error extracting missing skills: {e}")
        return []

def extract_matched_skills(req: evaluate_fit_request) -> list:
    try:
        resume_text: str = req.resume_text
        job_description: str = req.job_description

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        matched_skills = resume_skills & job_skills

        return list(matched_skills)
    except Exception as e:
        print(f"Error extracting matched skills: {e}")
        return []