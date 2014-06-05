#!/usr/bin/python

import nltk
import random

everything={}
while True:
	a = raw_input("Write text here:").lower()
	if a:
		tokens = ["START"]
		tokens.extend(nltk.word_tokenize(a))
		tokens.append("END")
		bigrams = nltk.bigrams(tokens)
		for bigram in bigrams:
			if bigram[0] in everything.keys():
				everything[bigram[0]].append(bigram[1])
			else:
				everything[bigram[0]]=[bigram[1]]
	current_token = "START"
	final_sentence_components = []	
	while current_token in everything.keys():
		possibilities = everything[current_token]
		current_token = random.choice(possibilities)
		final_sentence_components.append(current_token)
		final_sentence_components[0]=final_sentence_components[0].title()
 	print	' '.join(final_sentence_components[:-1]) + "."

			


