import Adafruit_DHT


DHT_SENSOR = Adafruit_DHT.DHT4
DHT_PIN = 4

def setDHT_pin(dht_pin):
  global DHT_PIN
  DHT_PIN = dht_pin


def get_Temperature():
  
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
  
    if humidity is not None and temperature is not None:
        return (temperature)
    else:
        return ("Failed to retrieve data!")

def BToN(BinaryNum):
    BinaryNum = list(BinaryNum)
    BinaryNum.reverse()
    NormalNum = 0
    CNum = 1
    for char in BinaryNum:
        if(char == "1"):
            NormalNum = NormalNum + CNum
            CNum = 2*CNum
        elif char == "0":
            CNum += 1
            
    return NormalNum

def NToB(NormalNum):
    NormalNum = int(NormalNum)
  
    BinaryNumL = []
    BinaryNumS = ""
    
    while NormalNum != 0:
        if (NormalNum/2) % 2 == True:
            BinaryNumL.append("0")
            NormalNum = NormalNum/2
        else:
            BinaryNumL.append("1")
            NormalNum = NormalNum/2-0.5

    BinaryNumL.reverse()
    for char in BinaryNumL:
        BinaryNumS += char
        
    return BinaryNumS

while True:
  print(get_Temperature())

