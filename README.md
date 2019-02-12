# DictionaryCracker
Simple python program to help crack substitution ciphers using a dictionary method

## Running the Program
To run in terminal:
```python DictionaryCracker.py [CIPHERTEXT]```

## Using Dictionaries
A simple one has been included with the application. 
Different versions can be found online. To read correctly, make sure that each new word is on a newline

## Known Issues
- Cannot deal with more than 26 unique chars
- Single threaded, struggles with large dictionaries when providing percentage completion
- O(2n) speed when analysing dictionary words, could be improved
- Currently reads through entire dictionary. Is there a faster way to go straight to the section required?

