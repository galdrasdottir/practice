

def count(cap):

	i = 0
	numbers = []

	while i < cap:
		print("At the top i is %d" % i)
		numbers.append(i)

		i = i + 1 
		print("Numbers now: ", numbers)
		print("At the bottom i is %d" % i)


count(6)
count(8)



