# src/config.py
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class MissingAPIKey(RuntimeError):
    """Raised when the LLM API key is not configured."""


def get_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise MissingAPIKey(
            "OPENAI_API_KEY is missing. Copy .env.example to .env and set it."
        )
    return key


if __name__ == "__main__":
    print(get_api_key()[:7] + "...")