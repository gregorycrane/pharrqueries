import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "tlg0012.tlg002.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

def printGrkSent(inputWord, inputCite):
    for sentence in root.findall('.//sentence'):
        sentid = sentence.get('id')
        for word in sentence.findall('./word'):
            lemma = word.get('lemma')
            cite = word.get('cite')
            if (cite != None):
                strippedCite = "Hom. Od. " + cite[32:]
                if (inputWord == lemma and inputCite == strippedCite):
                    return sentid

def returnOdyssey(inputWord, inputCite):
    targetid = printGrkSent(inputWord, inputCite)
    for sentence in root.findall('.//sentence'):
        sentid = sentence.get('id')
        if (sentid == targetid):
            for word in sentence.findall('./word'):
                form = word.get('form')
                lemma = word.get('lemma')
                if (inputWord == lemma):
                                     #  bold        green               end
                    sys.stdout.write('\033[1m' + '\33[32m' + form + '\033[0m')
                    sys.stdout.write(" ")
                else:
                    sys.stdout.write(form)
                    sys.stdout.write(" ")
    print("")