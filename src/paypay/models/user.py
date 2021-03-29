from dataclasses import dataclass
from typing import Optional


@dataclass()
class User:
    username: str
    password: str
    token: Optional[str] = None
    id: Optional[int] = None
