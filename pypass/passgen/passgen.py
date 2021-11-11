from dataclasses import dataclass
from hashlib import blake2b
from os import urandom


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
        return password
