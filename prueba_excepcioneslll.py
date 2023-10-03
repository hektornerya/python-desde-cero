def evaluaEdad(edad):

	if edad<0:
		raise TypeError("no negativo")

	if edad<20:
		return "muy joven"
	if edad<40:
		return "joven"
	if edad<60:
		return "mature"
	if edad<100:
		return "cuidate"

print(evaluaEdad(15))

