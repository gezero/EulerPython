start =100
end =1000

max = 0
for x in range(start,end):
	for y in range(start,end):
		val = x*y
		if str(val) == str(val)[::-1]:
			if val>max:
				max = val

print(max)