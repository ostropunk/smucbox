import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 as rc

reader = rc()

try:
    with open('testuri.txt', 'r') as f:
        uf = f.readlines()
        print(uf)
        for uri in uf:
            text = uri.strip()
            print('Now place tag to writer')
            reader.write(text)
            print('Written: ', text)
            input('Press any key.')
finally:
    GPIO.cleanup()