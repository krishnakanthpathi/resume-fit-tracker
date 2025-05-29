from fastapi import FastAPI

from app.models.request_models import evaluate_fit_request
from app.models.response_models import health_response, version_response

from typing import List , Optional , Dict

from app.services.fit_score_engine import get_fit_response , get_fit_response_all

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
    return get_fit_response(resquest)

@app.post("/evaluate-fit-all")
async def evaluate_fit_all(resquest: List[evaluate_fit_request]):
    return get_fit_response_all(resquest)
    