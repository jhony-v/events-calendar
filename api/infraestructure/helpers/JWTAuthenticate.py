from config import CONFIG_JWT_KEY
import jwt

class JWTAuthenticate:
    def decode(self, payload: str):
        return jwt.decode(payload.encode(), key=CONFIG_JWT_KEY)

    def encode(self, payload: dict):
        return jwt.encode(payload=payload, key=CONFIG_JWT_KEY).decode()
