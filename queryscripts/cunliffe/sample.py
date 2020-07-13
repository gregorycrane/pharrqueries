
from iliad import returnIliad
from odyssey import returnOdyssey
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "cunliffe.lexentries.unicode-copy.xml"

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}
tree = ET.parse(FILENAME)
root = tree.getroot()

inputWord = input("Enter a lemma to search the Cunliffe Lexicon. ")

for entry in root.findall(".//TEI:div[@type='textpart']", ns):
	wordEntry = entry.get('n')
	wordCode = entry.get('{http://www.w3.org/XML/1998/namespace}id')
	if (wordEntry != None):
		if (wordEntry == inputWord):
			print("Found " + inputWord + "!")
			while(True):
				print("Choose one of the following options. Type 'Quit' to exit.")
				print("   ", "|")
				print("    ", "->", "Full Entry")
				print("   ", "|")
				print("    ", "->", "Gloss")
				print("   ", "|")
				print("    ", "->", "Citations")
				print("   ", "|")
				print("    ", "->", "Quit")

				userInput = input("Enter: ")
				if (userInput == "Full Entry"):
					for head in entry.findall("./TEI:head", ns):
						head = head.get("id")
						for p in entry.findall("./TEI:p", ns):
							print(head, p.text)
						for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
							for head2 in subCat.findall("./TEI:head", ns):
								head2 = head2.get("id")
								for p in subCat.findall("./TEI:p", ns):
									print(head2, p.text)
					print("")

				elif (userInput == "Gloss"):
					for head in entry.findall("./TEI:head", ns):
						head = head.get("id")
						for gloss in entry.findall("./TEI:gloss", ns):
							print(head, gloss.text)
						for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
							for head2 in subCat.findall("./TEI:head", ns):
								head2 = head2.get("id")
								for gloss in subCat.findall("./TEI:gloss", ns):
									print(head2, gloss.text)
					print("")

				elif (userInput == "Citations"):
					for head in entry.findall("./TEI:head", ns):
						head = head.get("id")
						for bibl in entry.findall(".//TEI:bibl", ns):
							biblEntry = bibl.get('n')
							print(head, biblEntry)
							if (biblEntry.startswith('Hom. Il.')):
								returnIliad(wordEntry, biblEntry)
								print("")
								print("")
							else:
								returnOdyssey(wordEntry, biblEntry)
								print("")
								print("")
						for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
							for head2 in subCat.findall("./TEI:head", ns):
								head2 = head2.get("id")
								for bibl in subCat.findall(".//TEI:bibl", ns):
									biblEntry = bibl.get('n')
									print(head2, biblEntry)
									if (biblEntry.startswith('Hom. Il.')):
										returnIliad(wordEntry, biblEntry)
										print("")
										print("")
									else:
										returnOdyssey(wordEntry, biblEntry)
										print("")
										print("")
				elif (userInput == 'Quit'):
					break
				else:
					print("Invalid command.")
					print("")
