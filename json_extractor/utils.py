import json
from pathlib import Path


def read_json_template(file_path: Path):
    with file_path.open('r', encoding='utf-8') as file:
        return json.load(file)

def save_json_result(file_path: Path, data: dict):
    with file_path.open('w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

def read_raw_data(file_path: Path):
    return file_path.read_text(encoding='utf-8')