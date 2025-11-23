import secrets
import base64


def generate_api_key():
    random_bytes = secrets.token_bytes(32)
    api_key = base64.b64encode(random_bytes).decode("utf-8")
    return api_key


if __name__ == "__main__":
    print(generate_api_key())
