import sys
import xml.etree.ElementTree as ET
tree = ET.parse('/mnt/c/Users/bella/OneDrive/Documents/GitHub/pharrqueries/editedxml/pharr-ocr-copy.xml')
root = tree.getroot()

def printVocabSection(target):

	for div in root.findall('./{http://www.tei-c.org/ns/1.0}div'):
		lessonNum = div.get('n')

		for item in div.findall('./{http://www.tei-c.org/ns/1.0}item'):
			lemma = item.get('lemma')

			if (target == lemma):
	                            #  bold        green                                end
				sys.stdout.write('\033[1m' + '\33[32m' + '[Lesson ' + lessonNum + ']' + '\033[0m')
				sys.stdout.write(" ")