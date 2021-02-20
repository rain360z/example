i = 0
while i < 1000
	count = str(input())
	acount = int(count[-1])
	ccount = int(count)
	f = open('resault.txt', 'w')
	if acount == 0 or acount == 5 or acount == 6 \
	or acount == 7 or acount == 8 or acount == 9:
		print(count, 'программистов')
	elif acount == 1:
		if ccount == 1:
			print(count, 'программист')
		elif int(count[-1]) == int(count[-2]):
			print(count, 'программистов')
		else:
			print(count, 'программист')
	else:
		if ccount == 2 or ccount == 3 or ccount == 4:
			print(count, 'программиста')
		elif int(count[-1]) + int(count[-2]) == 2 \
		or int(count[-1]) + int(count[-2]) == 3 \
		or int(count[-1]) + int(count[-2]) == 4 \
		or int(count[-1]) + int(count[-2]) == 5 :
			print(count, 'программистов')
		else:
			print(count, 'программиста')
	i += 1


