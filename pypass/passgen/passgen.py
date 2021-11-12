from dataclasses import dataclass
from hashlib import blake2b
from os import urandom
import random


@dataclass(frozen=True)
class PasswordGenerator:
    """A class to generate secure passwords."""

    def generate(self, length: int = 10, **constraints: bool) -> str:

        # Generate salt for password generation
        salt: bytes = urandom(blake2b.SALT_SIZE)

        # Generate random number that will be used for password generation
        data: bytes = urandom(length)

        # Create the hash instance
        generator = blake2b(data, salt=salt, digest_size=length // 2)

        # Generate the password and convert it from bytes to string
        password: str = generator.hexdigest()

        # Update the password string based on the additional constraints
        # If uppercase is an additional constraint
        if constraints.get("uppercase"):

            # infinite loop
            while True:

                # get a random character from the string
                index = random.randrange(0, len(password))

                # if the character is an alphabetical character
                if password[index].isalpha():

                    # make the character uppercase and exit the infinite loop
                    password = password[0:index] + \
                        password[index].upper() + password[index+1:]
                    break

        # if special characters is an additional constraint
        if constraints.get("special"):

            # infinite loop
            while True:

                # get a random character from the string
                index = random.randrange(0, len(password))

                # if the character is a lowercase alphabetical character or a
                # numerical character
                if (password[index].isalpha() and password[index].islower()) \
                        or password[index].isnumeric():

                    # exchange the character with a valid special character and
                    # exit the infinite loop
                    password = password[0:index] + \
                        random.choice([".", ",", "!", "@", "_"]
                                      ) + password[index+1:]
                    break

        # return the final resulting password
        return password
