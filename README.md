# Word Saver
Application to save word meanings, sentences and (user-fed) mnemonics into MySQL DB

## word_meanings_filestream.py
Main Python File that reads the words.txt lines, gets the word meanings using PyDictionary, gets user input for mnemonic and saves in MySQL DB.

## WordMeaningsDB
Package that provides functions to save the word in DB. (Only used by word_meanings_filestream.py)

## WordMeaningsSaver
Contains standalone file that provides takes words as user input, gets the word meanings using PyDictionary, gets user input for mnemonic and saves in MySQL DB.
(Does not depend on WordMeaningsDB)

### Change Requirements
Update the config files with your preferred DB details
