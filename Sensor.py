import serial
import datetime as dt
from SensorData import SensorData
import sys

class Sensor:
	arduino = serial.Serial("/dev/ttyUSB0", 9600)

	@classmethod
	def getData(self):
		try:
			data = int(self.arduino.readline())
			time = dt.datetime.now().strftime('%H:%M:%S.%f')
			return SensorData(data, time)
		except KeyboardInterrupt:
			sys.exit()
		except:
			print("Can not convert data!")
			return None
