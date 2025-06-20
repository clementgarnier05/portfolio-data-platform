# strava_auth.py
import time
import json
import requests
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CRED_PATH = os.path.join(HERE, "credentials.json")
STRAVA_TOKEN_URL = "https://www.strava.com/oauth/token"

def update_strava_tokens() -> None:
    """
    Met à jour access_token, refresh_token et token_limit dans credentials.json.
    """
    with open(CRED_PATH, "r") as f:
        creds = json.load(f)

    now = int(time.time())
    need_refresh = False

    # Premier échange : grant_type=authorization_code
    if not creds.get("refresh_token") and creds.get("code"):
        payload = {
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
            "code": creds["code"],
            "grant_type": "authorization_code"
        }
        need_refresh = True
    # Renouvellement
    elif now >= creds.get("token_limit", 0):
        payload = {
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
            "grant_type": "refresh_token",
            "refresh_token": creds["refresh_token"]
        }
        need_refresh = True

    if not need_refresh:
        return

    resp = requests.post(STRAVA_TOKEN_URL, data=payload)
    resp.raise_for_status()
    data = resp.json()

    creds.update({
        "access_token": data["access_token"],
        "refresh_token": data["refresh_token"],
        "token_limit": data["expires_at"]
    })
    with open(CRED_PATH, "w") as f:
        json.dump(creds, f, indent=2)

def get_access_token() -> str:
    """Retourne un access_token valide, en mettant à jour si nécessaire."""
    update_strava_tokens()
    with open(CRED_PATH, "r") as f:
        return json.load(f)["access_token"]