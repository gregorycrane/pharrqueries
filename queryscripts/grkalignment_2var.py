# from pharr_vocab import printVocabSection

import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "tlg0012.tlg002.perseus-grc1.tb.xml"
tree = ET.parse(FILENAME)
root = tree.getroot()

def printGrkSent2(targetid, firstid, secondid):
    for sentence in root.findall('.//sentence'): 
        sentid = sentence.get('id')
        if (sentid == targetid):
            for word in sentence.findall('./word'):
                wordid = word.get('id')
                form = word.get('form')
                lemma = word.get('lemma')
                postag = word.get('postag')
                if (postag != None):
                    if (wordid == firstid or wordid == secondid):

                        # comment out if converting to html
                                        #  bold        green               end
                        sys.stdout.write('\033[1m' + '\33[32m' + form + '\033[0m')
                        sys.stdout.write(" ")
                        # printVocabSection(lemma)

                        # for html file conversion
                        # sys.stdout.write('<b>' + form + '</b>')
                        # sys.stdout.write(" ")

                        continue
                    sys.stdout.write(form)
                    sys.stdout.write(" ")