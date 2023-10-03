class Coche():
	def desplazamiento(self):
		print("me desplazo 4 ruedas")

class Moto():
	def desplazamiento(self):
		print("me desplazo 2 ruedas")

class Camion():
	def desplazamiento(self):
		print("me desplazo 6 ruedas")

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo)