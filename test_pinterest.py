import os
import requests

token = os.environ.get("PINTEREST_TOKEN")

if not token:
    print("❌ لم يتم العثور على التوكن في Secrets!")
    exit(1)

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.get("https://api.pinterest.com/v5/user_account", headers=headers)

print(f"كود الاستجابة: {response.status_code}")
print(response.json())

