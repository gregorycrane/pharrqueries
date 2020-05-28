import xml.etree.ElementTree as ET
tree = ET.parse('[insert path to xml file]')
root = tree.getroot()

# For purposes of counting number of results
count = 1

# Prints out input message
print("NOTE: Inputted letters must not have any breathings, accents, or subscripts.")
# Takes in specified letter to query for
letter = input("Input letter: ")

for body in root.findall('./body'): 
    for sentence in body.findall('./sentence'):

        # Takes in subdoc value
        subdoc = sentence.get('subdoc')

        # Sets bool value for whether the subdoc is within Iliad Book 1
        isBookOne = subdoc.startswith('1.')

        if(isBookOne):
            for word in sentence.findall('./word'):
                form = word.get('form')

                if (letter in form):
                    print(count, form)
                    count += 1
