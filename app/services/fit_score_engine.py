from typing import Dict, Any , List

from app.models.request_models import evaluate_fit_request
from app.models.response_models import evaluate_fit_response
from app.models.common_models import learning_step

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.services.skill_extractor import extract_missing_skills, extract_matched_skills
from app.services.learning_paths_extractor import learning_steps_extractor

from json import load, JSONDecodeError
from sentence_transformers import SentenceTransformer, util


def fit_score_calculater_v2(req: evaluate_fit_request) -> float:
    try:
        resume_text: str = req.resume_text
        job_description_text: str = req.job_description

        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode([resume_text, job_description_text], convert_to_tensor=True)
        cosine_sim = util.pytorch_cos_sim(embeddings[0], embeddings[1])

        return float(cosine_sim.item())
    except Exception as e:
        print(f"Error in fit_score_calculater_v2: {e}")
        return 0.0

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

def get_fit_response(req: evaluate_fit_request) -> evaluate_fit_response:
    try:
        missing_skills : list = extract_missing_skills(req)
        matched_skills : list = extract_matched_skills(req)
        fit_score : int  = fit_score_calculater(req) # or fit_score_calculater_v2(req)
        verdict : str = get_verdict(fit_score) 
        recommended_learning_track : List[learning_step]  = learning_steps_extractor(missing_skills , verdict)
        response : evaluate_fit_response = evaluate_fit_response(
            fit_score=fit_score,
            verdict=verdict,
            missing_skills=missing_skills,
            matched_skills=matched_skills,
            recommended_learning_track=recommended_learning_track,
            status="ok"
        )
        return response
    except Exception as e:
        return evaluate_fit_response(
            fit_score=0,
            verdict="error",
            missing_skills=[],
            matched_skills=[],
            recommended_learning_track=[],
            status="error",
        )

def get_fit_response_all(req: List[evaluate_fit_request]) -> List[evaluate_fit_response]:
    try:
        responses = []
        for request in req:
            response = get_fit_response(request)
            responses.append(response)
        return responses
    except Exception as e:
        print(f"Error in get_fit_response_all: {e}")
        return [evaluate_fit_response(
            fit_score=0,
            verdict="error",
            missing_skills=[],
            matched_skills=[],
            recommended_learning_track=[],
            status="error",
        )]