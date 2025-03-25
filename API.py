data = {
    "grant_type": "authorization_code",
    "client_id": "3426517866057797",
    "client_secret": "Oc2zx1Skan5FQouMDv26LIaTu2xADg5t",
    "code": "TG-67e2a48a0f6a1a0001f82193-333848565",
    "redirect_uri": "https://www.google.com.br"
}

response = requests.post("https://api.mercadolibre.com/oauth/token", data=data)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Erro {response.status_code}: {response.json()}")
    
##Access Token: APP_USR-3426517866057797-032508-8d5459a2989c06d5d123b0e7c16400b9-333848565

###############################################################################################################################
import requests
import csv
from google.colab import files

search_query = "Google Home, Apple TV, Amazon Fire TV"
url = f"https://api.mercadolibre.com/sites/MLA/search?q={search_query.replace(' ', '+')}&limit=50" 

access_token = "APP_USR-3426517866057797-032508-8d5459a2989c06d5d123b0e7c16400b9-333848565"  
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"API access error: {response.status_code}")
    print(response.json())

items = data.get('results', [])

file_path = '/content/mercadolivre_results.csv'  

with open(file_path, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Item ID", "Title", "Price", "Currency", "Available Quantity", "Category Id"])
    
    for item in items:
        writer.writerow([item.get("id"), item.get("title"), item.get("price"), item.get("currency_id"), item.get("available_quantity"), item.get("category_id")])

print(f"Data Saved: {file_path}")

files.download(file_path)