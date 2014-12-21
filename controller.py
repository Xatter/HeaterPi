import smbus
import time

bus = smbus.SMBus(1)
address = 0x02

def readNumber():
	number = bus.read_byte(address)
	return number

while True:
	time.sleep(1)
	number = readNumber()
	print "Arduino: ", number
