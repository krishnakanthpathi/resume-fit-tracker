import json
from typing import List , Dict

def clean_text(text: str) -> str:
    text = text.lower()  # Normalize to lowercase
    text = text.strip() 
    text = normalize_text(text)  # Normalize skill aliases
    
    res = []
    for char in text:
        if char.isalnum() or char.isspace():
            res.append(char)
    return ''.join(res).strip().lower()

def normalize_text(text: str) -> str:
    with open('app/data/config.json', 'r') as file:
        config = json.load(file)
        skill_alias = config.get('skill_alias', {})
        
    for alias, normalized in skill_alias.items():
        text = text.replace(alias, normalized)
        
    return text
