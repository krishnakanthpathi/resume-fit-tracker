import json
from app.models.common_models import learning_step
from typing import List

# Load learning paths from JSON file
try:
    with open('app/data/learning_paths.json', 'r') as opened_file:
        learning_paths = json.load(opened_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading learning paths: {e}")
    learning_paths = {}
    
# Load configuration from JSON file
try:
    with open("app/data/config.json", "r") as config_file:
        config = json.load(config_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading config: {e}")
    config = {}

 
def paths_extractor(missig_skills: list) -> List[learning_step]:
    extracted_paths = []
    for skill in missig_skills:
        if skill in learning_paths:
            try:
                learning_path = learning_step(
                    skill=skill,
                    steps=learning_paths[skill]
                )
                extracted_paths.append(learning_path)
            except Exception as e:
                print(f"Error creating learning_step for skill '{skill}': {e}")

    return extracted_paths

def learning_steps_extractor(skills: str, verdict: str) -> List[learning_step]:
    extracted_steps = paths_extractor(skills)
    learning_steps_cutoffs = config.get("learning_steps_cutoffs", {})
    no_of_steps = learning_steps_cutoffs.get(verdict, 0)

    if no_of_steps == 0:
        return []

    for learning_path in extracted_steps:
        try:
            learning_path.steps = learning_path.steps[:no_of_steps]
        except Exception as e:
            print(f"Error slicing steps for skill '{learning_path.skill}': {e}")

    return extracted_steps