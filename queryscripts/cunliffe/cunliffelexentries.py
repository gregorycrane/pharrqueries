from iliad import returnIliad
from odyssey import returnOdyssey
from returnForms import returnForms
import sys
import re
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "cunliffe.lexentries.unicode-copy.xml"

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}
tree = ET.parse(FILENAME)
root = tree.getroot()

def parseLexEntries(input):
	for entries in root.findall(".//TEI:div[@type='entry']", ns):
		wordEntry = entries.get('n')
		if (wordEntry != None):
			for gloss in entries.findall('.//TEI:gloss', ns):
				if (input == wordEntry):
					print("Gloss:", gloss.text)

	# for entries in root.findall(".//TEI:div[@type = 'textpart']", ns):
	# 	wordEntry = entries.get('n')
	# 	if (wordEntry != None):
	# 		if (wordEntry == input):
	# 			for p in entries.findall('.//TEI:p', ns):
	# 				for gloss in p.findall(".//TEI:gloss", ns):
	# 					print("Gloss:", gloss.text)
	# 					for quote in p.findall(".//TEI:gloss/../TEI:cit/TEI:quote", ns):
	# 						sys.stdout.write("Quote: ")
	# 						splitQuote = re.split("\s", quote.text)
	# 						forms = returnForms(input)
	# 						for i in splitQuote:
	# 							# for j in forms:
	# 							# 	if (i == j):
	# 							# 						#  bold        green               end
	# 							# 		sys.stdout.write('\033[1m' + '\33[32m' + i + '\033[0m')
	# 							# 		sys.stdout.write(" ")
	# 							# 		break;
	# 							# if (i == j):
	# 							# 	continue
	# 							# else:
	# 							sys.stdout.write(i)
	# 							sys.stdout.write(" ")
	# 						for bibl in p.findall(".//TEI:gloss/../TEI:cit/TEI:bibl", ns):
	# 							biblEntry = bibl.get('n')
	# 							print("(" + biblEntry + ")")
	# 							if (biblEntry.startswith('Hom. Il.')):
	# 								returnIliad(wordEntry, biblEntry)
	# 								print("")
	# 								print("")
	# 							else:
	# 								returnOdyssey(wordEntry, biblEntry)
	# 								print("")
	# 								print("")
	# 			for bibl in entries.findall(".//TEI:gloss/../TEI:bibl", ns):
	# 				biblEntry = bibl.get('n')
	# 				print(biblEntry)
	# 				if (biblEntry.startswith('Hom. Il.')):
	# 					returnIliad(wordEntry, biblEntry)
	# 					print("")
	# 					print("")
	# 				else:
	# 					returnOdyssey(wordEntry, biblEntry)
	# 					print("")
	# 					print("")