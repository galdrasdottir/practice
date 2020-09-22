class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)


happy_bday = Song(["Happy Birthday to you",
					"I don't want to get sued",
					"so I'll stop right there."])

bulls_on_parade = Song(["They rally around the family",
						"wich pockets full of shells"])

she_ra = "We're on the edge of greatness etc."

sing_she_ra = Song([she_ra])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

sing_she_ra.sing_me_a_song()

print("Let's make up a song! Give me three lines:")
first_line = input("1: ")
second_line = input("2: ")
third_line = input("3: ")

new_song = Song([first_line, second_line, third_line])

new_song.sing_me_a_song()