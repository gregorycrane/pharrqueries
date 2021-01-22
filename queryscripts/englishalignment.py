import sys

import xml.etree.ElementTree as ET
tree = ET.parse('atmurray.odyssey-sentalign-copy.xml')
#tree = ET.parse('/mnt/c/Users/bella/OneDrive/Documents/GitHub/pharrqueries/editedxml/atmurray.iliad-sentalign-copy.xml')
root = tree.getroot()



def printEngSent(target):

	for body in root.findall('.//{http://www.tei-c.org/ns/1.0}body'):
		for translation in body.findall('./{http://www.tei-c.org/ns/1.0}div'):
			for book in translation.findall('./{http://www.tei-c.org/ns/1.0}div'):
				for card in book.findall('./{http://www.tei-c.org/ns/1.0}div'):
					for p in card.findall('./{http://www.tei-c.org/ns/1.0}p'):
						for s in p.findall('./{http://www.tei-c.org/ns/1.0}s'):
							id = s.get('{http://www.w3.org/XML/1998/namespace}id')
							#print(id) #for debugging the english xml
							if (target == id[4:11]):
								sys.stdout.write(s.text)
