from sys import argv

script, username = argv

print("Hello %r! What file would you like to read?" % username)
txt = input("> ")

print("Here's your file %r:" % txt)
print(txt.read())

