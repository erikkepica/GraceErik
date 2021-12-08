import requests
import Adafruit_DHT

url="https://gracewebapp-erikznider.online404.repl.co/api/dht/"
apikey="test"

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

headers = {
    "Authorization" : "Bearer " + apikey
}

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
  data = {
    "temp" : temperature,
    "hum" : humidity
  }

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
