import os, inspect
from PyDictionary import PyDictionary
from pathlib import Path


class Saver:
    def __init__(self, meaningPath, rejectPath):
        self.dictionary = PyDictionary()

        self.curPath = meaningPath
        self.rejPath = rejectPath
        self.word_meanings = None
        self.reject_file = None
        self.wmPath = os.path.join(self.curPath, 'word-meanings.txt')
        self.rjPath = os.path.join(self.rejPath, 'reject-file.txt')
    
    #Self Sufficient Loop
    def loop(self):
        continue_prog = 'y'

        self.word_meanings = open(self.wmPath, 'a+')
        self.reject_file = open(self.rjPath, 'a+')

        while(self.continue_prog=='y'):
            word = input('Select the word that you want: ')
            meaning = self.dictionary.meaning(word)
            print(f'{word}: {meaning}')

            self.save_word_exec(word, meaning)

            continue_prog = input('Continue[y/n]: ')
        
        self.word_meanings.close()
        self.reject_file.close()
    
    #Open Meaning File
    def open_file(self):
        self.word_meanings = open(self.wmPath, 'a+')
        self.reject_file = open(self.rjPath, 'a+')

    #Save Word Meaning in the File
    def save_word(self, word):

        meaning = self.dictionary.meaning(word)
        print(f'{word}: {meaning}')

        self.save_word_exec(word, meaning)
        
    
    #Close Meaning File
    def close_file(self):
        self.word_meanings.close()
        self.reject_file.close()
    

    def save_word_exec(self, word, meaning):
        save = input('Is this correct?[y/n]: ')

        if (save=='y'):
            print('Saving word')
            mnemonic = input('Give a mnemonic: ')
            result = self.word_meanings.write(f'{word}| {meaning}| {mnemonic}\n')
            print(result)
        else:
            print('Saving as reject')
            result = self.reject_file.write(word)
            print(result)


