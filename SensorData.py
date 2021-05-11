import serial
import time

class SensorData:
	def __init__(self, data, time):
		self.data = data
		self.time = time
