import sys

import xml.etree.ElementTree as ET
tree = ET.parse('/mnt/c/Users/bella/OneDrive/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg001.perseus-grc1.tb.xml')
root = tree.getroot()

tree1 = ET.parse('/mnt/c/Users/bella/OneDrive/Documents/GitHub/Homerica/murray.iliad3.xml')
root1 = tree1.getroot()

def printEngSent(target):
    for TEI in root1.findall('./TEI'):
 #   for body in root1.findall('./body'):
        print("hi")
"""         for p in body.findall('./p'):
            for sentence in p.findall('./s'):
                id = sentence.get('xml:id')
                id[4:10]
                print(id) """

# prints out entire sentence 
def printSent(target):

    for body in root.findall('./body'): 
        for sentence in body.findall('./sentence'):
            
            # Takes in id value
            id = sentence.get('id')

            if (id == target):
                for word in sentence.findall('./word'):
                    form = word.get('form')
                    postag = word.get('postag')

                    sys.stdout.write(form)
                    sys.stdout.write(" ")

# For purposes of counting number of results
count = 1

# Prints out input message
print("Please input the lemma of a vocabulary word for all known examples of the word in Iliad 1.")
# Takes in specified vocab word to query for
vocab = input("Input lemma: ")

for body in root.findall('./body'): 
    for sentence in body.findall('./sentence'):

        # Takes in subdoc value
        subdoc = sentence.get('subdoc')
        # Takes in id value
        id = sentence.get('id')

        # Sets bool value for whether the subdoc is within Iliad Book 1
        isBookOne = subdoc.startswith('1.')

        if(isBookOne):
            for word in sentence.findall('./word'):
                form = word.get('form')
                lemma = word.get('lemma')
                cite = word.get('cite')

                if (vocab == lemma):
                    print(count, "form: ", form, "lemma: ", lemma, cite)
                    printSent(id)
                    printEngSent(id)
                    print('')
                    print('')
                    count += 1
