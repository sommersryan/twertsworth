import json, markovify, random, logging
from config import MIN_CHAR, MAX_CHAR, ATTEMPTS, ENCODING

def writePoem(textModel, seedWords, tweetPrefix):
	modelKeys = list(textModel.chain.model)
	tweetRoom = MAX_CHAR - len(tweetPrefix) #need to keep track of how many chars we have for the tweet
	random.shuffle(seedWords)
	for word in seedWords:
		if word == 'person':
			continue
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
						if MIN_CHAR <= len(poem) <= tweetRoom:
							logging.info("Satisfied conditions in %s attempts",t)
							
							#Capitalize first letter
							
							listChars = list(poem)
							listChars[0] = listChars[0].upper()
							finalPoem = "".join(listChars)
							return tweetPrefix + finalPoem
					else:
						logging.info('Could not use this key pair')
	logging.info("None of the seed words worked")
	genericPoem = textModel.make_short_sentence(tweetRoom)
	listChars = list(genericPoem)
	listChars[0] = listChars[0].upper()
	finalPoem = "".join(listChars)
	return tweetPrefix + finalPoem