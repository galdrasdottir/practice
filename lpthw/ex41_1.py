from urllib import request
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

#load up the words from the website
for word in request.urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

	words = WORDS.most_common(50)

print(words)