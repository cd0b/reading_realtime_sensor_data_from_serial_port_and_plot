import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Sensor import Sensor

class Animator:
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	xs = []
	ys = []
	sensor = Sensor()

	def animate(self, delay):
		return animation.FuncAnimation(self.fig, self.step, fargs=(self.xs, self.ys), interval=delay)

	def show(self):
		plt.show()

	def step(self, i, xs, ys):
		sensorData = self.sensor.getData()
		if(sensorData == None):
			return 

		self.xs.append(sensorData.time)
		self.ys.append(sensorData.data)
		print(sensorData.data)

		self.xs = self.xs[-20:]
		self.ys = self.ys[-20:]

		self.ax.clear()
		self.ax.plot(self.xs,self.ys)
		
		plt.xticks(rotation=45, ha='right')
		plt.subplots_adjust(bottom=0.30)
		plt.title("Sensor Graph")
		plt.ylabel("data")
