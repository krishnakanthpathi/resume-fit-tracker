"""

file: app/models.py
description: The Inputs and Outputs are validated using Pydantic models.

"""

from typing import List, Optional
from pydantic import BaseModel

# Request Model
class evaluate_fit_request(BaseModel):
    resume_text: str
    job_description: str

# Learning Step
class learning_step(BaseModel):
    skill: str
    steps: List[str]

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
