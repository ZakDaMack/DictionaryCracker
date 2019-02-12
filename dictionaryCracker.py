# Python Dictionary Cracker for Substitution Ciphers
# Author: Zak Dowsett
# Version: 1.0.0
# Apache 2.0 License

import math
import sys

# currently o(2n) speed
def AnalyseWord(word):
    wordUpper = word.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charArray = []
    for char in wordUpper:
        # if char is not in array, add to array to collect unique characters
        if char not in charArray:
            charArray.append(char)
            
    wordToReturn = ""
    for char in wordUpper:
	# Assign each letter to a unique character
        wordToReturn = wordToReturn + alphabet[charArray.index(char)]
        
    return wordToReturn    

def main(ciphertext):
    # analyse word
    cipherlength = len(ciphertext)
    analysedCipher = AnalyseWord(ciphertext)
    
    # open dictionary and start reading
    dictPath = "englishdictionary.txt"
#    dictPath = "crackstation.txt"
    dict = open(dictPath, "r")
    print("Calculating file size...")
    numberOfLines = sum(1 for line in open(dictPath, "r"))
    print("Starting...")

    percentageDone = 0.0
    linesIterated = 0

    possibleWords = []
    for word in dict:
	word = word.strip()
        if len(word) == cipherlength:
            if AnalyseWord(word) == analysedCipher:
                possibleWords.append(word)
                print(word)
	linesIterated = linesIterated + 1
	prevPercentage = percentageDone
	percentageDone = int(math.floor((linesIterated * 100) / numberOfLines))
	if percentageDone > prevPercentage:
	    print("Percentage complete: " + str(percentageDone) + "%")

    print("Dictionary search complete. Words found: " + str(len(possibleWords)))
    

ciphertext = ""
if len(sys.argv) > 1:
    ciphertext = sys.argv[1]
else:
    ciphertext = raw_input("Enter ciphertext: ")
main(ciphertext)
