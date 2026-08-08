import os
import requests

token = os.environ.get("PINTEREST_TOKEN")

if not token:
    print("❌ خطأ: لم يتم العثور على التوكن!")
    exit(1)

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.get("https://api.pinterest.com/v5/user_account", headers=headers)

print(f"كود الاستجابة: {response.status_code}")
print(response.json())
