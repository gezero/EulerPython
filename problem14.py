stop=1000001
memory =[0]*stop
memory[1]=1

def algorithm(n):
	if n>stop:
		return -1 	
	if memory[n]!=0:		
		return memory[n] 
	memory[n] = 1+(algorithm(n//2) if n%2 ==0 else algorithm(n*3+1))	
	return memory[n]
	

max = 0
n=0
for x in range(1,100000):
	a = algorithm(x)
	if a>max:
		max = a
		n=x
		print (max)
		print (n)
