import requests
import json
import os

def fetch_data():
    token = os.environ.get('PINTEREST_TOKEN')
    url = "https://api.pinterest.com/v1/me/boards/"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    
    # سنطبع حالة الرد دائماً لنرى ماذا يقول Pinterest
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        with open('my_data.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("Success: Data saved")
    else:
        # هنا سنعرف المشكلة الحقيقية
        print("Failed to fetch data")
        print("Response Text:", response.text)

if __name__ == "__main__":
    fetch_data()
    
