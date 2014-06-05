#!/usr/bin/python

import nltk
import random

everything={}
while True:
	a = raw_input("Write text here:").lower()
	tokens = ["START"]
	tokens.extend(nltk.word_tokenize(a))
	bigrams = nltk.bigrams(tokens)
	for bigram in bigrams:
		if bigram[0] in everything.keys():
			everything[bigram[0]].append(bigram[1])
		else:
			everything[bigram[0]]=[bigram[1]]
	current_token = "START"	
	while current_token in everything.keys():
		possibilities = everything[current_token]
		current_token = random.choice(possibilities)
		print current_token
			


