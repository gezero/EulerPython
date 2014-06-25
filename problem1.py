def count_multipliers_of_3_5(a,b):
	sum=0
	for x in range(a,b):
		if x%3==0 or x%5==0:
			sum+=x
			pass
	return sum

print(count_multipliers_of_3_5(1,10))
print(count_multipliers_of_3_5(1,1000))