from fastapi import FastAPI
from passgen import PasswordGenerator

passgen_app = FastAPI(title="Password Generator")


@passgen_app.post("/api/passgen")
async def generate_password(body: dict = {"length": 10}):
    generator = PasswordGenerator()
    password = generator.generate(**body)
    return password
