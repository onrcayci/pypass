from fastapi import APIRouter

from .passgen import PasswordGenerator

passgen_router = APIRouter(prefix="/passgen")


@passgen_router.post("")
async def generate_password(body: dict = {"length": 10}):
    print(body)
    generator = PasswordGenerator()
    password = generator.generate(**body)
    return password
