import requests
import json
import os

def fetch_pinterest_data():
    token = os.environ.get('PINTEREST_TOKEN')
    # الرابط المحدث لـ API الإصدار الخامس v5
    url = "https://api.pinterest.com/v5/boards"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            with open('my_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("نجاح! تم حفظ البيانات في my_data.json")
        else:
            print("فشل الاتصال ببنترست")
            print("الرسالة التي عاد بها الخادم:", response.text)
            
    except Exception as e:
        print(f"حدث خطأ برمجياً: {e}")

if __name__ == "__main__":
    fetch_pinterest_data()
    
