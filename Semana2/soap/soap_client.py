from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Luis")
print(result)

result1 = client.service.SumaDosNumeros(a=2)
print(result1)