from config import GITHUB_TOKEN
import httpx

url = "https://api.github.com/user"

headers = {"Authorization": f"Bearer {GITHUB_TOKEN}" }


response = httpx.get(url, headers=headers)

print(response.status_code)
print(response.json()["login"])