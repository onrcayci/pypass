from dataclasses import dataclass
from hashlib import blake2b
from os import urandom
import random


@dataclass(frozen=True)
class PasswordGenerator:

    def generate(self, length: int = 10, **constraints: bool) -> str:
        # Generate salt for password generation
        salt: bytes = urandom(blake2b.SALT_SIZE)
        # Generate random number that will be used for password generation
        data: bytes = urandom(length)
        # Create the hash instance
        generator = blake2b(data, salt=salt, digest_size=length // 2)
        password: str = generator.hexdigest()
        if constraints.get("uppercase"):
            while True:
                index = random.randrange(0, len(password))
                if password[index].isalpha():
                    password = password[0:index] + \
                        password[index].upper() + password[index+1:]
                    break
        if constraints.get("special"):
            while True:
                index = random.randrange(0, len(password))
                if password[index].islower():
                    password = password[0:index] + \
                        random.choice([".", ",", "!", "@", "_"]
                                      ) + password[index+1:]
                    break
        return password
