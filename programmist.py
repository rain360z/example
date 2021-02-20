i = 0
while i < 1000:
	count = str(input())
	acount = int(count[-1])
	ccount = int(count)
	f = open('resault.txt', 'w')
	if acount == 0 or acount == 5 or acount == 6 \
	or acount == 7 or acount == 8 or acount == 9:
		f.write(count, 'программистов', \n)
	elif acount == 1:
		if ccount == 1:
			f.write(count, 'программист', \n)
		elif int(count[-1]) == int(count[-2]):
			f.write(count, 'программистов', \n)
		else:
			f.write(count, 'программист', \n)
	else:
		if ccount == 2 or ccount == 3 or ccount == 4:
			f.write(count, 'программиста', \n)
		elif int(count[-1]) + int(count[-2]) == 2 \
		or int(count[-1]) + int(count[-2]) == 3 \
		or int(count[-1]) + int(count[-2]) == 4 \
		or int(count[-1]) + int(count[-2]) == 5 :
			f.write(count, 'программистов', \n)
		else:
			f.write(count, 'программиста', \n)
	i += 1
	f.сlose()

