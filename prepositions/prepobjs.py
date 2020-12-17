import xml.etree.ElementTree as ET
import pandas as pd

LOCALPATH = '/Users/bellahwang/Documents/GitHub/gAGDT/data/xml/tlg0012.tlg001.perseus-grc1.tb.xml'

tree = ET.parse(LOCALPATH)
root = tree.getroot()

count=1         #sets counter keeping track of query results
prepid=10001    #in case the code encounters a prep first
wordhead=10000  #in case the code encounters a noun first
LEMMA = 'ἀμφί'  #change as needed
CASE = 'a'      #change as needed
prepdict = {}
nodeps = 0

for body in root.findall('./body'): 
    for sentence in body.findall('./sentence'):
        prepcount = 0
        matchlist = []
        for word in sentence.findall('./word'):
            if 'postag' in word.attrib:
                postag = word.get('postag')
                case = postag[7] #narrows down to case
                lemma = word.get('lemma')
                if lemma == LEMMA:
                    prepid = word.get('id')
                    prepcount += 1
                    #print(word.attrib)
                else: 
                    wordhead = word.get('head')
                    if prepid == wordhead:
                        matchlist.append('T')
                        if case == CASE:
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
                    else:
                        matchlist.append('F')
        numpreps = matchlist.count('T')
        if (numpreps != prepcount):
            extra = abs(numpreps - prepcount)
            nodeps += extra
        prepid = 10001
        wordhead = 10000

#list1 = prepdict.values()
#print(sum(list1))
sortedDict = sorted(prepdict.items(), key=lambda x: x[1], reverse=True)

df = pd.DataFrame(sortedDict)
df.to_csv('prepobjs.csv', index=False)

print(*sortedDict, sep = '\n')
print("No dependent objs:", nodeps)