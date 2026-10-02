"""GitHub API client: checks whether the user pushed any commits today."""
from datetime import datetime, timezone

import httpx

from config import GITHUB_TOKEN

GITHUB_API = "https://api.github.com"
USERNAME = "juliavalerialopez"

def did_commit_today(username: str = USERNAME) -> bool:
    """Return True if the user has at least one PushEvent today (UTC)."""
    url = f"{GITHUB_API}/users/{username}/events"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}" }

    response = httpx.get(url, headers=headers)
    response.raise_for_status() #stop with a clear error on 401/404 instead of failing later

    #GitHub timestamp are UTC ( "...Z"), so compare against today's UTC date
    #TODO switch to Europe/Amsterdam time; late-evening pushes currently count as the wrong day
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    pushes = [event for event in response.json()
              if event["type"] == "PushEvent" and event["created_at"].startswith(today)]

    return len(pushes) > 0

if __name__ == "__main__":
    #Runs only when you execute this file directly: pytohn github_client.pyy): 
    print(did_commit_today())