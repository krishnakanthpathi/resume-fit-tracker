from typing import List, Optional
from pydantic import BaseModel
from app.models.common_models import learning_step

# Response Model
class evaluate_fit_response(BaseModel):
    fit_score: float
    verdict: str
    matched_skills: List[str]
    missing_skills: List[str]
    recommended_learning_track: List[learning_step]
    status: str

# Health Check Model
class health_response(BaseModel):
    status: str

# Version Info Model
class version_response(BaseModel):
    model_version: str
