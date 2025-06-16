import re
import json
from typing import List


def clean_text(text: str) -> str:
    text = text.lower().strip()  # Lowercase and trim
    text = normalize_text(text)  # Normalize aliases from config.json
    res = []
    for char in text:
        if char.isalnum() or char.isspace() or char in ['.', ',', '-', '_', '@', '#', '/', '%', '&', '*']:
            res.append(char)
    return ''.join(res).strip()


def normalize_text(text: str) -> str:
    try:
        with open('app/data/config.json', 'r') as file:
            config = json.load(file)
            skill_alias = config.get('skill_alias', {})
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading skill_alias: {e}")
        skill_alias = {}

    for alias, normalized in skill_alias.items():
        pattern = r'\b{}\b'.format(re.escape(alias))
        text = re.sub(pattern, normalized, text)

    return text

