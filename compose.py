import json, markovify, random
from config import MIN_CHAR, MAX_CHAR, ATTEMPTS, ENCODING

def writePoem(textModel, seedWords):
	modelKeys = list(textModel.chain.model)
	
	for word in seedWords:
		results = [v for i, v in enumerate(modelKeys) if v[0] == word]
		if results:
			random.shuffle(results) # shuffle the model key pairs so we don't always get the same seed for a poem from similar images
			for result in results:
				for t in range(0,ATTEMPTS):
					poem = textModel.make_sentence_with_start(' '.join(result))
					if MIN_CHAR <= len(poem) <= MAX_CHAR:
						print ("took " + str(t) + " attempts")
						return poem
	return textModel.make_short_sentence(140)