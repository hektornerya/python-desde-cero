class Vehiculos():

	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True
	def acelarar(self):
		self.acelera=True
	def frenar(self):
		self.frena=True
	def estado(self):
		print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
		 self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "Cargada"
		else:
			return "Sin carga"

class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy d cbllt"
	def estado(self):
		print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
		 self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia=100
	def cargarEnergia(self):
		self.cargando(True)

miMoto=Moto("hnd", "cbr")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Rnlt", "kng")
miFurgoneta.arrancar()	
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BiciElectrica(VElectricos, Vehiculos):
	pass

miBici=BiciElectrica("orbe", "bn15")
