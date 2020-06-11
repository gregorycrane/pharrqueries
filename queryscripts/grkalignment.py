from pharr_vocab import printVocabSection
import sys
import xml.etree.ElementTree as ET
#tree = ET.parse('/mnt/c/Users/bella/OneDrive/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg001.perseus-grc1.tb.xml')
tree = ET.parse('/Users/bellahwang/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg001.perseus-grc1.tb.xml')
root = tree.getroot()

# prints out entire sentence 
def printGrkSent(target, wordform):

    for body in root.findall('./body'): 
        for sentence in body.findall('./sentence'):
            
            # Takes in id value
            id = sentence.get('id')

            if (id == target):
                for word in sentence.findall('./word'):
                    form = word.get('form')
                    lemma = word.get('lemma')
                    postag = word.get('postag')
                    if (postag != None):
                        if (form == wordform):
                                            #  bold        green               end
                            sys.stdout.write('\033[1m' + '\33[32m' + form + '\033[0m')
                            sys.stdout.write(" ")
                            printVocabSection(lemma)
                            continue
                        sys.stdout.write(form)
                        sys.stdout.write(" ")