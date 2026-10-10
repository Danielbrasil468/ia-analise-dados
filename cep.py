 
import requests
cep = input( "Digite o seu CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"
dados = requests.get(url)
resposta = dados.json()
print(resposta)   
print(f"Você mora na rua {resposta["logradouro"]} bairro {resposta["bairro"]} cidade de {resposta["localidade"]}")