import json, markovify, random, logging
from config import MIN_CHAR, MAX_CHAR, ATTEMPTS, ENCODING, EXCLUDE_WORDS

def writePoem(textModel, seedWords, tweetPrefix):
	modelKeys = list(textModel.chain.model)
	#track chars available for poem
	tweetRoom = MAX_CHAR - len(tweetPrefix)
	stanzaLength = int(tweetRoom / 2) - 1
	random.shuffle(seedWords)
	stanzas = []
	
	for word in seedWords:
		
		if len(stanzas) == 2:
			finalPoem = tweetPrefix + '\r'.join(stanzas)
			return finalPoem
		
		if word in EXCLUDE_WORDS:
			continue
		
		logging.info('Trying %s',word)
		results = [v for i, v in enumerate(modelKeys) if v[0] == word]
		logging.info('Found %s model key pairs',len(results))
		
		if results:
			random.shuffle(results) 
			
			for result in results:
				logging.info('Trying the pair %s',' '.join(result))
				stanza = textModel.make_short_sentence(stanzaLength, init_state=result)
				logging.info('Text model responded: %s',stanza)
				if stanza:
					logging.info("Satisfied conditions in %s attempts",t)							
					stanzas.append(formatLine(stanza))
					break		
				logging.info('Could not use this key pair')
	
	if len(stanzas) == 1:
		stanzaTwo = textModel.make_short_sentence(stanzaLength)
		stanzas.append(formatLine(stanzaTwo))
		finalPoem = tweetPrefix + '\r'.join(stanzas)
		return finalPoem
		
	logging.info("None of the seed words worked")
	genericPoem = textModel.make_short_sentence(tweetRoom)
	finalPoem = tweetPrefix + formatLine(genericPoem)
	return finalPoem
	
def formatLine(line):
	words = [list(a) for a in line.split()]
	words[0][0] = words[0][0].upper()
	words[1][0] = words[1][0].lower()
	newLine = [[char.replace(',','\r') for char in word] for word in words]
	formatted = ' '.join([''.join(letter) for letter in newLine])
	return formatted