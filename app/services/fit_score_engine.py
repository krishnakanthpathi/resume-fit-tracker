from typing import Dict, Any

from app.models.request_models import evaluate_fit_request

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from json import load, JSONDecodeError


def fit_score_calculater(req: evaluate_fit_request) -> float:
    try:
        resume_text: str = req.resume_text
        job_description_text: str = req.job_description

        
        vectorizer = TfidfVectorizer(stop_words='english')

        tfidf_matrix = vectorizer.fit_transform([resume_text, job_description_text])

        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

        return float(cosine_sim[0][0])
    except Exception as e:
        print(f"Error in fit_score_calculater_v2: {e}")
        return 0.0

def get_verdict(score: float) -> str:
    try:
        with open("app/data/config.json", "r") as file:
            config = load(file)

        cutoffs: Dict[str, float] = config["fit_score_cutoffs"]

        if score >= cutoffs["strong_fit"]:
            return "strong_fit"
        elif score >= cutoffs["moderate_fit"]:
            return "moderate_fit"
        else:
            return "weak_fit"
    except (FileNotFoundError, JSONDecodeError, KeyError) as e:
        print(f"Error in get_verdict: {e}")
        return "unknown"
