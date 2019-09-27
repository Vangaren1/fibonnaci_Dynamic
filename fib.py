def fib(a):
	num = {0:0,1:1}
	def fib1(b):
		print("Inside fib1")
		if b in num:
			print("Returned base case")
			print(b)
			return num[b]
		else:
			print("adding to index of values")
			num[b]=fib1(b-1)+fib1(b-2)
			print("returning new index")
			return num[b]
	return fib1(a)

print(fib(10))

print("https://github.com/Vangaren1/fibonnaci_Dynamic.git")



