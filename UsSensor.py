import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 24
echo = 23

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)

    start_time =  time.time()
    end_time = time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()
    
    while GPIO.input(echo) == 1:
        end_time = time.time()

    time_diffrance = end_time - start_time

    distance = ((time_diffrance * 342)/2) * 100

    return distance

if __name__ == "__main__":
  try:
    while True:
        distance = distance()
        print("Izmerjena razdalja je", distance, "cm")
        time.sleep(0.2)
  except KeyboardInterrupt:
      print("Uporabnik je pritisnil ctrl + c!")
      GPIO.cleanup()