from fastapi import FastAPI

from app.models.response_models import evaluate_fit_response
from app.models.request_models import evaluate_fit_request
from app.models.response_models import health_response, version_response
from app.models.common_models  import learning_step

from typing import List , Optional , Dict

from app.services.skill_extractor import extract_missing_skills, extract_matched_skills
from app.services.fit_score_engine import fit_score_calculater , get_verdict
from app.services.learning_paths_extractor import paths_extractor , learning_steps_extractor
from app.services.fit_score_engine import fit_score_calculater_v2

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Resume Fit Evaluation API!"}

@app.get("/health")
async def health_check():
    return health_response(status="ok")

@app.get("/version")
async def version_info():
    return version_response(model_version="1.0.0")

@app.post("/evaluate-fit")
async def evaluate_fit(resquest: evaluate_fit_request):
    try:
        missing_skills : list = extract_missing_skills(resquest)
        matched_skills : list = extract_matched_skills(resquest)
        fit_score : int  = fit_score_calculater_v2(resquest)
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
