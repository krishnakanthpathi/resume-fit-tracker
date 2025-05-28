from typing import List, Optional
from pydantic import BaseModel

# Request Model
class evaluate_fit_request(BaseModel):
    resume_text: str
    job_description: str
