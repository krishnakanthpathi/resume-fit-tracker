from pandas import read_csv
from functools import cache

from app.utils.text_cleaner import clean_text

from app.models.request_models import evaluate_fit_request

from spacy import load
from spacy.matcher import PhraseMatcher


try:
    df = read_csv('app/data/skills_dataset.csv', names=['skills'])
    skills = df['skills']
except Exception as e:
    print(f"Error loading skills dataset: {e}")
    skills = []

try:
    nlp = load("en_core_web_sm")
    
    patterns = [nlp.make_doc(skill.lower()) for skill in skills]

    matcher = PhraseMatcher(nlp.vocab ,  attr="LOWER")
    matcher.add("SKILLS", patterns)

except OSError:
    print("Spacy model 'en_core_web_sm' not found.'")
    nlp = None

@cache
def extract_skills(text: str) -> set:
    text = clean_text(text)
    doc = nlp(text)
    matches = matcher(doc)
    
    found_skills = set()
    for match_id, start, end in matches:
        span = doc[start:end]
        found_skills.add(span.text)
        
    return found_skills
        
      
def extract_missing_skills(req: evaluate_fit_request) -> list:
    try:
        resume_text: str = req.resume_text
        job_description: str = req.job_description
        # print(resume_text)
        # print(job_description)
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)
        # print(f"Resume Skills: {resume_skills}")
        # print(f"Job Skills: {job_skills}")
        # Find skills in job description that are not in resume
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