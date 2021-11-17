import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, SHT_PIN)
    
    if humidity is not None and temperature is not None:
        print("Temperatura znasa:", temperature, "vlaga pa", humidity)
    else:
        print("Fail")
