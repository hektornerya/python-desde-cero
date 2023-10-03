class coche():

	def __init__(self):

			self.__lgChasis=250
			self.__anChasis=120
			self.__ruedas=4
			self.__enmarcha=False

	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
				chequeo=self.__chequeo_interno()	

		if(self.__enmarcha and chequeo):
			return "En marcha"
		elif(self.__enmarcha and chequeo==False):
			return "algo anda mal chequeo No arranca"
		else:
			return "Parado"

	def estado(self):
		print("el coche tiene: ", self.__ruedas, " ruedas. Ancho ", self.__anChasis, " y de largo ",
		self.__lgChasis)

	def __chequeo_interno(self):
		print("realizando chq inter ")

		self.gasolina = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False	

miCoche=coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("----------cargamos segundo objeto------------")

miCoche2=coche()
print(miCoche2.arrancar(False))
miCoche2.estado()