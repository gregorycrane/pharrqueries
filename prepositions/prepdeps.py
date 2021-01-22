import xml.etree.ElementTree as ET
import pandas as pd

LOCALPATH = '/Users/bellahwang/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg001.perseus-grc1.tb.xml'

tree = ET.parse(LOCALPATH)
root = tree.getroot()

count = 1         #sets counter keeping track of query results
verbid = 1000    #in case the code encounters a verb first
prephead = 1001  #in case the code encounters a prep first
LEMMA = 'ὑπό'  #change as needed
verblemma = 'tester'
prepdict = {}

for body in root.findall('./body'): 
    for sentence in body.findall('./sentence'):
        for word in sentence.findall('./word'):
            if 'postag' in word.attrib:
                postag = word.get('postag')
                pos = postag[0]
                
                if (pos == 'r'):
                    preplemma = word.get('lemma')
                    if preplemma == LEMMA:
                        prephead = word.get('head')
                        if verbid == prephead:
                            objcount = prepdict.get(verblemma)
                            if (objcount == None):
                                prepdict.update({verblemma: 1})
                            else:
                                objcount += 1
                                prepdict.update({verblemma: objcount})
                        #print(word.attrib)
                elif (pos == 'v'):
                    verbid = word.get('id')
                    verblemma = word.get('lemma')
                    if verbid == prephead:
                        objcount = prepdict.get(verblemma)
                        if (objcount == None):
                            prepdict.update({verblemma: 1})
                        else:
                            objcount += 1
                            prepdict.update({verblemma: objcount})
                            #print(word.attrib)
                            #print(count) #counts query results
                            #count+=1
        verbid = 1000
        prephead = 1001

#list1 = prepdict.values()
#print(sum(list1))

sortedDict = sorted(prepdict.items(), key=lambda x: x[1], reverse=True)
df = pd.DataFrame(sortedDict)
df.to_csv('prepdeps.csv', index=False)

print(*sortedDict, sep = '\n')