edad=input("tu edad es: ")

while(edad.isdigit()==False):
	print("pon numeros")
	edad=input("tu edad es: ")
if(int(edad)<18):
	print("no pasas")
else:
	print("pasas")
