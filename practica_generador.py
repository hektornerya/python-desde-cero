def generapares(limite):

	num=1

	while num<limite:
		yield num*2
		num=num+1

devuelvepares=generapares(10)

for i in devuelvepares:
	print(i)
