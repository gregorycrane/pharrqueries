from englishalignment import printEngSent
from grkalignment import printGrkSent

import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "/Users/bellahwang/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg001.perseus-grc1.tb.xml"
tree = ET.parse(FILENAME)
root = tree.getroot()

count = 1

print("Please input the lemma of a vocabulary word for all known examples of the word in Iliad 1.")
vocab = input("Input lemma: ")

for sentence in root.findall('.//sentence'):
    subdoc = sentence.get('subdoc')
    sentid = sentence.get('id')
    for word in sentence.findall('./word'):
        wordid = word.get('id')
        form = word.get('form')
        lemma = word.get('lemma')
        cite = word.get('cite')
        if (vocab == lemma):
            print(count, "form: ", form, "lemma: ", lemma, "cite: ", cite)
            printGrkSent(sentid, wordid)
            print('')
            printEngSent(sentid)
            print('')
            print('')
            count += 1

            # for html file conversion
            # sys.stdout.write("\t" + "<tr>" + "\n")
            # sys.stdout.write("\t" + "\t" + "<td>" + form + "</td>" + "\n")
            # sys.stdout.write("\t" + "\t" + "<td>" + lemma + "</td>" + "\n")
            # sys.stdout.write("\t" + "\t" + "<td>" + cite + "</td>" + "\n")
            # sys.stdout.write("\t" + "\t" + "<td>")
            # printGrkSent(sentid, wordid)
            # sys.stdout.write("</td>" + "\n")
            # sys.stdout.write("\t" + "\t" + "<td>")
            # printEngSent(sentid)
            # sys.stdout.write("\t" + "\t" + "</td>" + "\n")
            # sys.stdout.write("\t" + "</tr>" + "\n")

