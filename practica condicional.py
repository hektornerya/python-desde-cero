print("asignaturas 2017")
print("optativas: info grafica - pba soft - usab y acces")
opcion=input("Escoge asignatura: ")

asignatura=opcion.lower()

if asignatura in ("info grafica","pba soft","usab y acces"):
	print("elegi: " + asignatura)
else:
	print("no existe")

