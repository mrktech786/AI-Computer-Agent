import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

def _bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}

@dataclass(frozen=True)
class Settings:
    require_approval: bool = _bool("AGENT_REQUIRE_APPROVAL", True)
    terminal_enabled: bool = _bool("AGENT_ALLOW_TERMINAL", False)

settings = Settings()
