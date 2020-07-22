import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt

# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

G = nx.DiGraph()

verbid = None
attribhead = None
# generalcount = 1
# verbcount = None
# attribcount = None

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
				G.add_node(verblemma, lemma = verblemma, pos = pos, cite = verbcite)
				# verbcount = generalcount
				# generalcount += 1
			else:
				attribhead = word.get('head')
				attriblemma = word.get('lemma')
				attribcite = word.get('cite')
				attribrelation = word.get('relation')
				
			if (attribhead == verbid):
				# print("attrib:", attriblemma)
				G.add_node(attriblemma, lemma = attriblemma, pos = pos, cite = attribcite)
				# attribcount = generalcount
				# generalcount += 1

				# print(verblemma + " is modified by " + attriblemma)
				G.add_edge(verblemma, attriblemma, relation = attribrelation)

nx.write_graphml(G, "verbNetworkDirected.graphml")
# nx.draw(G)
# plt.show()
