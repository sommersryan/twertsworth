import json, markovify, random, logging
from config import MIN_CHAR, MAX_CHAR, ATTEMPTS, ENCODING

def writePoem(textModel, seedWords):
	modelKeys = list(textModel.chain.model)
	
	for word in seedWords:
		logging.info('Trying %s',word)
		results = [v for i, v in enumerate(modelKeys) if v[0] == word]
		logging.info('Found %s model key pairs',len(results))
		if results:
			random.shuffle(results) # shuffle the model key pairs so we don't always get the same seed for a poem from similar images
			for result in results:
				logging.info('Trying the pair %s',' '.join(result))
				for t in range(0,ATTEMPTS):
					poem = textModel.make_sentence_with_start(' '.join(result))
					logging.info('Text model responded: %s',poem)
					if poem:
						if MIN_CHAR <= len(poem) <= MAX_CHAR:
							logging.info("Satisfied conditions in %s attempts",t)
							return poem
					else:
						logging.info('Could not use this key pair')
	logging.info("None of the seed words worked")
	return textModel.make_short_sentence(140)