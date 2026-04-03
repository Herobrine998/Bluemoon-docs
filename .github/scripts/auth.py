import json
import jwt
import time
import requests

with open("key.json") as f:
    sa = json.load(f)

now = int(time.time())

payload = {
    "iss": sa["client_email"],
    "scope": "https://www.googleapis.com/auth/drive",
    "aud": "https://oauth2.googleapis.com/token",
    "exp": now + 3600,
    "iat": now
}

token = jwt.encode(payload, sa["private_key"], algorithm="RS256")

r = requests.post(
    "https://oauth2.googleapis.com/token",
    data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": token
    }
)

print(r.json()["access_token"])
