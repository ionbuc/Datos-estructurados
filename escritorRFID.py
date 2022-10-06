import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('nuevo dato:')
        print("ahora acerca tu Tag")
        reader.write(text)
        print("Escrito")
finally:
        GPIO.clanup()

