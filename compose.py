import json, markovify, random, logging
from config import MIN_CHAR, MAX_CHAR, ATTEMPTS, ENCODING, EXCLUDE_WORDS

def writePoem(textModel, seedWords, tweetPrefix):
	modelKeys = list(textModel.chain.model)
	tweetRoom = MAX_CHAR - len(tweetPrefix) #need to keep track of how many chars we have for the tweet
	random.shuffle(seedWords)
	for word in seedWords:
		if word in EXCLUDE_WORDS:
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
							words = [list(a) for a in poem.split()] 
							#ensure capitalized first word, lower case second
							words[0][0] = words[0][0].upper()
							words[1][0] = words[1][0].lower()
							#recompose
							finalPoem = ' '.join([''.join(letter) for letter in words])
							return tweetPrefix + finalPoem
					else:
						logging.info('Could not use this key pair')
	logging.info("None of the seed words worked")
	genericPoem = textModel.make_short_sentence(tweetRoom)
	#split in to lists of words with lists of chars
	words = [list(a) for a in genericPoem.split()] 
	#ensure capitalized first word, lower case second
	words[0][0] = words[0][0].upper()
	words[1][0] = words[1][0].lower()
	#recompose
	finalPoem = ' '.join([''.join(letter) for letter in words])
	return tweetPrefix + finalPoem