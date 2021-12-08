import requests

url="https://gracewebapp-erikznider.online404.repl.co/api/dht/"
apikey="test"

data = {
  "temp" : "send from RPI",
  "hum" : "send from RPI"
}

headers = {
    "Authorization" : "Bearer " + apikey
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
