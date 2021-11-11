from fastapi import APIRouter

from .passgen import PasswordGenerator

passgen = APIRouter(prefix="passgen")


@passgen.post("")
async def generate_password(length: int = 10):
    generator = PasswordGenerator()
    password = generator.generate(length=length)
    return password
