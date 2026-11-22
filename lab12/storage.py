import json
from pathlib import Path
from logic import validate_records

def load_records(path):
    file_path = Path(path)
    if not file_path.exists():
        return [], False

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    validate_records(data)
    return data, True

def save_records(path, records):
    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
