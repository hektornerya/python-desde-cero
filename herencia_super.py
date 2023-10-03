class Persona():
	def __init__(self, nombre, edad, residencia):
		self.nombre=nombre
		self.edad=edad
		self.residencia=residencia
	def descripcion(self):
		print("nombre: ", self.nombre, "edad: ", self.edad, "residencia: ", self.residencia)

class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
		self.salario=salario
		self.antiguedad=antiguedad
	def descripcion(self):
		super().descripcion()
		print("salario: ", self.salario, "antiguedad: ", self.antiguedad)


tony=Empleado(1500, 50, "tony", 55, "mx")
tony.descripcion()
print(isinstance(tony, Persona))