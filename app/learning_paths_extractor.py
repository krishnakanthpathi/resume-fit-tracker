import json
from app.models import learning_step
from typing import List

def paths_extractor(missig_skills: list) -> List[learning_step]:
    extracted_paths = []
    
    with open('app/data/learning_paths.json', 'r') as opened_file:
        learning_paths = json.load(opened_file)
        
    for skill in missig_skills:
        if skill in learning_paths:
            learning_path = learning_step(
                skill=skill,
                steps=learning_paths[skill]
            )
            extracted_paths.append(learning_path)
            
    return extracted_paths

def learning_steps_extractor(skills: str, verdict: str) -> List[learning_step]:
    extracted_steps = paths_extractor(skills)
    
    with open("app/data/config.json", "r") as config_file:
        config = json.load(config_file)
        
    learning_steps_cutoffs = config.get("learning_steps_cutoffs", {})
    no_of_steps = learning_steps_cutoffs.get(verdict, 0)
    
    if no_of_steps == 0:
        return []
    
    for learning_path  in extracted_steps:
        learning_path.steps = learning_path.steps[:no_of_steps]
        
    return extracted_steps
    