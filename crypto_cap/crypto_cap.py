# crypto_cap
import requests, json

# api_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=SECRET-KEY") 
api_requests = requests.get("https://api.coinmarketcap.com/v1/ticker/") 

api = json.loads(api_requests.content)
print(api)

