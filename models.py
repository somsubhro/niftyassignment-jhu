from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Policy:
    effect: str
    principal: str
    action: str
    resource: str
    condition: Optional[str] = None

@dataclass
class Request:
    principal: Dict[str, str]  # e.g., {"id": "User::123"}
    action: str
    resource: Dict[str, str]   # e.g., {"id": "Document::abc", "owner": "User::123"}
