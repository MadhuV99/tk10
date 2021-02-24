# crypto_cap
import requests, json

api_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=42796342-84df-4c6b-8e36-1bb0b7e9c2ac") 
api = json.loads(api_requests.content)
print(api)

