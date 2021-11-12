from typer import Typer

from passgen import PasswordGenerator

passgen_cli = Typer(name="Password Generator")


@passgen_cli.command()
def generate_password(length: int = 10, uppercase: bool = False, special: bool = False):
    generator = PasswordGenerator()
    password = generator.generate(
        length=length, uppercase=uppercase, special=special)
    print(password)


if __name__ == "__main__":
    passgen_cli()
