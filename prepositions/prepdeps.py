import xml.etree.ElementTree as ET
import pandas as pd

LOCALPATH = '/Users/bellahwang/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg001.perseus-grc1.tb.xml'

tree = ET.parse(LOCALPATH)
root = tree.getroot()

count=1         #sets counter keeping track of query results
verbid=10001    #in case the code encounters a verb first
prephead=10000  #in case the code encounters a prep first
LEMMA = 'ἀμφί'  #change as needed
prepdict = {}

for body in root.findall('./body'): 
    for sentence in body.findall('./sentence'):
        for word in sentence.findall('./word'):
                lemma = word.get('lemma')
                if lemma == LEMMA:
                    prephead = word.get('head')
                    #print(word.attrib)
                else:
                    if 'postag' in word.attrib:
                        postag = word.get('postag')
                        pos = postag[0] #narrows down to pos
                        verbid = word.get('id')
                        if pos == 'v':
                            if verbid == prephead:
                                lemma = word.get('lemma')
                                objcount = prepdict.get(lemma)
                                if (objcount == None):
                                    prepdict.update({lemma: 1})
                                else:
                                    objcount += 1
                                    prepdict.update({lemma: objcount})
                                #print(word.attrib)
                                #print(count) #counts query results
                                #count+=1
        prepid = 10001
        wordhead = 10000

#list1 = prepdict.values()
#print(sum(list1))

sortedDict = sorted(prepdict.items(), key=lambda x: x[1], reverse=True)
df = pd.DataFrame(sortedDict)
df.to_csv('prepdeps.csv', index=False)

print(*sortedDict, sep = '\n')