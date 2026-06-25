import os
import requests
import json

# جلب التوكن من الإعدادات السرية في GitHub
token = os.getenv('PINTEREST_TOKEN')

# إعدادات الاتصال
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# الرابط الخاص بسحب معلومات حسابك الشخصي
url = 'https://api.pinterest.com/v5/user_account'

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        # حفظ البيانات في ملف my_data.json
        with open('my_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print("تم سحب البيانات بنجاح.")
    else:
        print(f"فشل الاتصال، كود الخطأ: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"حدث خطأ: {e}")
  print(f"Data retrieved: {data}")
                                         
