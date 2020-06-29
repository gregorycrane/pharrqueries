import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "/Users/bellahwang/Documents/GitHub/Homerica/pharr.homgramm.xml"

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}
tree = ET.parse(FILENAME)
root = tree.getroot()

def printVocabSection(target):
	for lesson in root.findall(".//TEI:div[@type = 'textpart']", ns):
		lessonNum = lesson.get('n')
		for vocab in lesson.findall(".//TEI:foreign", ns):
			lemma = vocab.text
			if (target == lemma and lessonNum != None):
							    #  bold        green                                end
				sys.stdout.write('\033[1m' + '\33[32m' + '[' + lessonNum + ']' + '\033[0m')
				sys.stdout.write(" ")