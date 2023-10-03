print("evaluacion alumons")

nota_alumno=input("introduce nota dl almn: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))