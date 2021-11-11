from typing import Dict
from fastapi import APIRouter

from .passgen import PasswordGenerator

passgen = APIRouter(prefix="/passgen")


@passgen.post("")
async def generate_password(body: dict = {"length": 10}):
    print(body)
    generator = PasswordGenerator()
    password = generator.generate(**body)
    return password
