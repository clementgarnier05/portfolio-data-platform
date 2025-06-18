# API.py
from strava_auth import get_access_token
import requests

BASE_URL = "https://www.strava.com/api/v3"

def get_activities(page: int = 1, per_page: int = 50, after: int = None, before: int = None) -> list:
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {"page": page, "per_page": per_page}
    if after:  params["after"] = after
    if before: params["before"] = before

    resp = requests.get(f"{BASE_URL}/athlete/activities", headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()