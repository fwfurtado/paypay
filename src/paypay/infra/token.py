from uuid import uuid4


class TokenService:
    def generate_toke(self) -> str:
        return str(uuid4())
