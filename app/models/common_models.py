from typing import List, Optional
from pydantic import BaseModel

# Learning Step
class learning_step(BaseModel):
    skill: str
    steps: List[str]