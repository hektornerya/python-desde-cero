valido=False

email=input("tu mail? ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("ok")
else:
	print("no ok")
