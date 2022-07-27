import requests

def obtener_dolar(url):

	querystring = {"type":"valoresprincipales"}

	payload = ""
	response = requests.request("GET", url, data=payload, params=querystring)

	print(response.text)

	return response.text