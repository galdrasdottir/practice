from sys import argv

script, username = argv

print("Hello %r! What file would you like to read?" % username)

txt = input("> ")
open_txt = open(txt)

print("Here's your file %r:" % txt)
print(open_txt.read())

open_txt.close()

