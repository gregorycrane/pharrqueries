# Use this one to run all the other scripts!

from cunliffelexentries import parseLexEntries
from cunliffehompers import parseHomPers

print("Enter a word to return the Cunliffe Lexicon entry for it.")
inputWord = input("Input: ")
print("")

print("Entries from cunliffe.lexentries.unicode.xml: ")
parseLexEntries(inputWord)

print("")
print("Entries from cunliffe.hompers.unicode.xml: ")
parseHomPers(inputWord)

