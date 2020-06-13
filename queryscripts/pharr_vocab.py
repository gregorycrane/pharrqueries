import sys
import xml.etree.ElementTree as ET
#tree = ET.parse('/mnt/c/Users/bella/OneDrive/Documents/GitHub/pharrqueries/editedxml/pharr-ocr-copy.xml')
tree = ET.parse('/Users/bellahwang/Documents/GitHub/Homerica/pharr.homgramm.xml')
root = tree.getroot()

def printVocabSection(target):
	for text in root.findall('./{http://www.tei-c.org/ns/1.0}text'):
		for body in text.findall('./{http://www.tei-c.org/ns/1.0}body'):
			for div in body.findall('./{http://www.tei-c.org/ns/1.0}div'):
				lessonNum = div.get('n')
				for p in div.findall('./{http://www.tei-c.org/ns/1.0}p'):
					for listElem in p.findall('./{http://www.tei-c.org/ns/1.0}list'):
						for item in listElem.findall('./{http://www.tei-c.org/ns/1.0}item'):
							for foreign in item.findall('./{http://www.tei-c.org/ns/1.0}foreign'):
								lemma = foreign.text
								#lemma = foreign.get('n')
							if (target == lemma):
						                        #  bold        green                                end
								sys.stdout.write('\033[1m' + '\33[32m' + '[' + lessonNum + ']' + '\033[0m')
								sys.stdout.write(" ")