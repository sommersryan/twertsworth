import json
import markovify

def loadModel(chainStore):
	with open(chainStore,'r') as chainFile:
		chainString = json.load(chainStore)
	return markovify.Text.from_chain(chainString)
	