import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt

# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

G = nx.Graph()

verbid = None
attribhead = None
generalcount = 1
verbcount = None
attribcount = None

for sentence in root.findall(".//sentence"):
	for word in sentence.findall("./word"):
		if ('postag' in word.attrib):
			postag = word.get('postag')
			pos = postag[0]
			if (pos == 'v'):
				verbid = word.get('id')
				verblemma = word.get('lemma')
				verbcite = word.get('cite')
				# print("verb:", verblemma)
				G.add_node(generalcount, lemma = verblemma, cite = verbcite)
				verbcount = generalcount
				generalcount += 1
			else:
				attribhead = word.get('head')
				attriblemma = word.get('lemma')
				attribcite = word.get('cite')
				attribrelation = word.get('relation')
				
			if (attribhead == verbid):
				# print("attrib:", attriblemma)
				G.add_node(generalcount, lemma = attriblemma, cite = attribcite)
				attribcount = generalcount
				generalcount += 1

				# print(verblemma + " is modified by " + attriblemma)
				G.add_edge(verbcount, attribcount, relation = attribrelation)

nx.write_graphml(G, "verbNetwork.graphml")
# nx.draw(G)
# plt.show()
