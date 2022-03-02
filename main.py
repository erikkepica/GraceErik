import RPi.GPIO as GPIO
import dht as DHT
import ultra_sonic_sensor as US
import Adafruit_GPIO_SPI as SPI
import Adafruit_SSD1306
from PIL import Image ,ImageDraw, ImageFont
import time, subprocess

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

try:
  trig = 26
  echo = 19
  US.initialize(trig, echo)

  dht_pin = 4
  DHT.setDHT_pin(dht_pin)
  while True:
    draw.rectangle((0, 0, width, height), outline = 0, fill = 0)

    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True)
    draw.text((x, top), "IP: " + str(IP), font = font, fill=255)
    
    distance = US.calculate_distance(trig, echo)
    draw.text((x, top+8), "Distaance: " + str("%.1f" % distance) + "cm", font = font, fill=255)

    data = DHT.get_humidity()
    draw.text((x, top+16), "Humidity: " + str(data[0]) + "%", font = font, fill=255)
    draw.text((x, top+24), "Temperature: " + str(data[1]) + "%", font = font, fill=255)

    disp.image(image)
    disp.display()

    time.sleep(2)
except KeyboardInterrupt:
  draw.rectangle((0, 0, width, height), outline = 0, fill = 0)













