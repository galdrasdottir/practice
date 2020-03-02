from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

check = input("Of %r, %r, and %r, which is your favourite? " % (first, second, third))

print("%r is my favourite too." % (check))