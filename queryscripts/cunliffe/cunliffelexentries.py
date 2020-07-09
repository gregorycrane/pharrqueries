from iliad import returnIliad
from odyssey import returnOdyssey
import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "cunliffe.lexentries.unicode.xml"

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}
tree = ET.parse(FILENAME)
root = tree.getroot()

def parseLexEntries(input):
	for entries in root.findall(".//TEI:div[@type = 'textpart']", ns):
		wordEntry = entries.get('n')
		if (wordEntry != None):
			if (wordEntry == input):
				for gloss in entries.findall(".//TEI:gloss", ns):
					print("Gloss:", gloss.text)

					for bibl in entries.findall(".//TEI:gloss/../TEI:bibl", ns):
						biblEntry = bibl.get('n')
						print(biblEntry)
						if (biblEntry.startswith('Hom. Il.')):
							returnIliad(wordEntry, biblEntry)
							print("")
							print("")
						else:
							returnOdyssey(wordEntry, biblEntry)
							print("")
							print("")