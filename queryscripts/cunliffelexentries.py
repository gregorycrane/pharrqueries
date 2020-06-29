from iliad import returnIliad
from odyssey import returnOdyssey
import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "/Users/bellahwang/Documents/GitHub/Homerica/cunliffe.lexentries.unicode.xml"

ns = {"TEI": "http://www.tei-c.org/ns/1.0",
	  "XML": "http://www.w3.org/XML/1998/namespace"}
tree = ET.parse(FILENAME)
root = tree.getroot()

def parseLexEntries(input):
	for entries in root.findall(".//TEI:div[@type = 'textpart']", ns):
		wordEntry = entries.get('n')
		if (wordEntry != None):
			if (wordEntry == input):
				for gloss in entries.findall(".//TEI:gloss", ns):
					print("Gloss:", gloss.text)
				for bibl in entries.findall(".//TEI:bibl", ns):
					biblEntry = bibl.get('n')
					print(biblEntry)
					returnIliad(wordEntry, biblEntry)
					returnOdyssey(wordEntry, biblEntry)
					print("")