import os, inspect
from pathlib import Path

from config import host, user, password, db, word_table, reject_table

curPath = os.getcwd()
#print(curPath)
progFile = Path(inspect.getfile(inspect.currentframe()))
progPath = progFile.parent

#from WordMeaningsSaver import word_meanings_saver
#Saver = word_meanings_saver.Saver('F:\Python_Projects\GRE\WordMeanings', 'F:\Python_Projects\GRE\WordMeanings')

from WordMeaningsDB import word_meanings_db

Saver = word_meanings_db.Saver(host, user, password, db, words_table, reject_table)

Saver.open_file()

os.chdir(progPath)
file = open('words.txt', 'r+')
#os.chdir(curPath)

Lines = file.readlines()
for line in Lines: 
    word = line.strip()
    Saver.save_word(word) 

    ask_cont = input('Continue [y/n]: ')
    if ask_cont=='n':
        break
    
file.close()

Saver.close_file()
