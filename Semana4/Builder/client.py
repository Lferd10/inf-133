import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

pizza = {
    "tamaño": "Grande",
    "masa": "Suave",
    "toppings": ["Jamon", "Queso", "Peperoni"]
}
response = requests.post(url, json=pizza, headers=headers)
print(response.json())