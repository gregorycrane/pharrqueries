from englishalignment import printEngSent
from grkalignment_2var import printGrkSent
import xml.etree.ElementTree as ET
tree = ET.parse("/Users/bellahwang/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg001.perseus-grc1.tb.xml")
root = tree.getroot()

count = 1		    #sets counter keeping track of query results
subjid = None 		#in case the code encounters a subjunctive first
anhead = None		#in case the code encounters an ἄν first
anform = None

for body in root.findall('./body'): 
	for sentence in body.findall('./sentence'):
        # Takes in subdoc value
		subdoc = sentence.get('subdoc')
        # Takes in id value
		id = sentence.get('id')
		for word in sentence.findall('./word'):
			if 'postag' in word.attrib:
				postag = word.get('postag')
				tense = postag[4] #narrows down to verb tense
				form = word.get('form')
				cite = word.get('cite')
				lemma = word.get('lemma')
				if lemma == 'ἄν':
					anhead = word.get('head')
					anform = word.get('form')
				else: #only other possibility is if the word is a subjunctive
					subjid = word.get('id')
					if anhead == subjid: #checks if ἄν modifies subjunctive
						if tense == 's':
							print(count, "form: ", form, "lemma: ", lemma, "cite: ", cite)
							printGrkSent(id, form, anform)
							print('')
							printEngSent(id)
							print('')
							print('')
							count+=1
