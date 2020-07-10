import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

list = []

def returnForms(inputWord):
    for word in root.findall('.//word'):
    	lemma = word.get('lemma')
    	if (lemma == inputWord):
	        form = word.get('form')
	        list.append(form)

    return list