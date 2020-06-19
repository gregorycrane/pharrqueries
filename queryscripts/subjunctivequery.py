import xml.etree.ElementTree as ET
tree = ET.parse("/Users/bellahwang/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg002.perseus-grc1.tb.xml")
root = tree.getroot()

count=1		#sets counter keeping track of query results
subjid=None 		#in case the code encounters a subjunctive first
anhead=None		#in case the code encounters an ἄν first

for body in root.findall('./body'): 
	for sentence in body.findall('./sentence'):
		print(sentence.attrib) 
		for word in sentence.findall('./word'):
			if 'postag' in word.attrib:
				postag = word.get('postag')
				tense = postag[4] #narrows down to verb tense
				lemma = word.get('lemma')
				if lemma == 'ἄν':
					anhead = word.get('head')
				else: #only other possibility is if the word is a subjunctive
					subjid = word.get('id')
					if anhead == subjid: #checks if ἄν modifies subjunctive
						if tense == 's':
							print(word.attrib)
							print(count) #counts query results
							count+=1
