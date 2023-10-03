def divide():

	try:	

		op1=(float(input("primer#: ")))
		op2=(float(input("segundo#: ")))

		print("division es: " + str(op1/op2))

	except ValueError:
		print("error en valor")

	except ZeroDivisionError:
		print("no div zero")

	print("final")

divide()
