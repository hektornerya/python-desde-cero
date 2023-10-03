import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("persona nueva con nombre ", self.nombre)

	def __str__(self):
		return"{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
	personas=[]
	def __init__(self):
		listaDePersonas=open("ficheroExterno", "ab+")
		listaDePersonas.seek(0)
		try:
			self.personas=pickle.load(listaDePersonas)
			print("se cargaron {} personas del ficheroExterno".format(len(self.personas)))
		except:
			print("fichero vacio")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("info ficheroext es: ")
		for p in self.personas:
			print(p)

milista=ListaPersonas()
persona=Persona("ana", "f", 25)
milista.agregarPersonas(persona)
milista.mostrarInfoFicheroExterno()
