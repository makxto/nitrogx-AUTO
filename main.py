import requests
import json
import uuid
import time
from config import config

url = config['url']
headers = config['headers']
file_path = config['file_path']
sleep_duration = config['sleep_duration']

while True:
    partner_user_id = str(uuid.uuid4())

    data = {
        'partnerUserId': partner_user_id,
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        print(f'Request Headers: {headers}')
        print(f'Request Payload: {json.dumps(data)}')
        print(f'Response Status Code: {response.status_code}')
        print(f'Response Content: {response.text}')

        try:
            json_data = response.json()
            token = json_data.get('token', '')

            promo_url = f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}'

            print(f'Promo URL: {promo_url}')

            with open(file_path, 'a') as file:
                file.write(promo_url + '\n' + '\n')

        except json.JSONDecodeError as json_err:
            print(f"Error decoding JSON: {json_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"Request Error: {req_err}")

    time.sleep(sleep_duration) 