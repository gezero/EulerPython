sum = 1000



for x in range(1,334):
	for y in range(1,501):
		numbers = sorted([x,y,1000-x-y])
		if (numbers[0]*numbers[0]+numbers[1]*numbers[1]==numbers[2]*numbers[2]):
			print(numbers)
			print(numbers[0]*numbers[1]*numbers[2])