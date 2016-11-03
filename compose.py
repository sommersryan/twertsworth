import json, markovify, random
from config import MIN_CHAR, MAX_CHAR, ATTEMPTS, ENCODING

def loadModel(corpus):
	with open(corpus,encoding=ENCODING) as corpusFile:
		return markovify.Text(corpusFile.read())

def writePoem(textModel, seedWords):
	modelKeys = list(textModel.chain.model)
	
	for word in seedWords:
		results = [v for i, v in enumerate(modelKeys) if v[0] == word]
		if results:
			random.shuffle(results) # shuffle the model key pairs so we don't always get the same seed for a poem from similar images
			for result in results:
				poem = textModel.make_sentence_with_start(' '.join(result))
				if MIN_CHAR <= poem <= MAX_CHAR:
					return poem