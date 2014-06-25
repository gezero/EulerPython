a = 1
b = 1
max =4000000
sum=0
while(a<max):
	c = a
	a = b+c
	b =c
	if (a%2 ==0):
		sum+=a
print(sum)