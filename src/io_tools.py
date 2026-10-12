import json
from pathlib import Path
from src.errors import DataValidationError

def ensure_dir(path: Path, data: dict) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path

def write_json(path: Path, data: dict) -> None:
    ensure_dir(path.parent)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        
def read_text_checked(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise DataValidationError(f"{path} is empty", column=None)
    return text