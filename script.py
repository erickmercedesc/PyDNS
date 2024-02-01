import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv('API_TOKEN')
zone_id = os.getenv('ZONE_ID')
dns_record_id = os.getenv('DNS_ID')
dns_name = os.getenv('DNS_NAME')

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

def update_cloudflare_dns(ip):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}'

    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
    }
    
    data = {
        'type': 'A',
        'name': dns_name,
        'content': ip,
        'ttl': 120,
        'proxied': False
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()

# Obtener la IP pública actual
public_id = get_public_ip() 
print(f'Public IP: {public_id}')

# # Actualizar el registro DNS en Cloudflare
response = update_cloudflare_dns(public_id)
print('RESPONSE:', response)
