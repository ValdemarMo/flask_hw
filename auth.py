import hashlib

SALT = "325 32rfewr3wqrf322###%Wa4"


def hash_password(password: str):
    password = f"{password}{SALT}"
    password = password.encode()
    return str(hashlib.md5(password))
