import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

def returnIliad(inputWord, inputCite):
    for word in root.findall('.//word'):
        form = word.get('form')
        lemma = word.get('lemma')
        cite = word.get('cite')
        if (cite != None):
            strippedCite = "Hom. Il. " + cite[32:]

            if (strippedCite == inputCite):
                if (inputWord == lemma):
                                     #  bold        green               end
                    sys.stdout.write('\033[1m' + '\33[32m' + form + '\033[0m')
                    sys.stdout.write(" ")
                else:
                    sys.stdout.write(form)
                    sys.stdout.write(" ")