import os, inspect
from PyDictionary import PyDictionary
import MySQLdb
import json
import traceback

from config import words_table, reject_table

class Saver:
    def __init__(self, host, user, password, db, words_table, reject_table):
        self.dictionary = PyDictionary()

        self.db = MySQLdb.connect(host, user, password, db)
        self.cursor = self.db.cursor()

        self.words_table = words_table
        self.reject_table = reject_table

        self.columns = '(word, mnemonic, example, Verb, Adjective, Noun, Adverb, Others)'
    
    #Self Sufficient Loop
    def loop(self):
        continue_prog = 'y'

        while(self.continue_prog=='y'):
            word = input('Select the word that you want: ')
            meaning = self.dictionary.meaning(word)
            print(f'{word}: {meaning}')

            self.save_word_exec(word, meaning)

            continue_prog = input('Continue[y/n]: ')
        
        self.db.close()
    
    #Open Meaning File
    def open_file(self):
        #self.word_meanings = open(self.wmPath, 'a+')
        #self.reject_file = open(self.rjPath, 'a+')
        pass

    #Save Word Meaning in the File
    def save_word(self, word):

        meaning = self.dictionary.meaning(word)
        print(f'{word}: {meaning}')

        self.save_word_exec(word, meaning)
        
    
    #Close Meaning File
    def close_file(self):
        self.db.commit()
        print('Closing DB')
        self.db.close()
    

    def save_word_exec(self, word, meaning):
        save = input('Is this correct?[y/n]: ')
        command = ''
        result = ''

        #self.removeTrash(meaning)

        if (save=='y'):
            (noun, adjective, adverb, verb, others) = self.processMeaning(meaning)
            
            print('Saving word')
            mnemonic = input('Give a mnemonic: ')
            example = input('Excellent! Now give an example: ')

            #columns = '(word, mnemonic, example, Verb, Adjective, Noun, Adverb, Others)'
            #columns = ''
            #Triple quotes because some strings have double quotes
            command = f"""INSERT INTO {self.words_table}{self.columns} VALUES(\"{word}\", \"{mnemonic}\", \"{example}\", \"{verb}\", \"{adjective}\", \"{noun}\", \"{adverb}\", \"{others}\")"""
            print(command)
        else:
            insert = input('Do you want to put your own meaning?[y/n]: ')

            if (insert=='y'):
                (noun, adjective, adverb, verb, others) = self.inputMeaning()
                mnemonic = input('Give a mnemonic: ')
                example = input('Excellent! Now give an example: ')

                command = f"""INSERT INTO {self.words_table}{self.columns} VALUES(\"{word}\", \"{mnemonic}\", \"{example}\", \"{verb}\", \"{adjective}\", \"{noun}\", \"{adverb}\", \"{others}\")"""
                print(command)

            else:
                print('Saving as reject')
                command = f"INSERT INTO {self.reject_table} VALUES(\"{word}\")"
        
        try:
            result = self.cursor.execute(command)
        except:
            traceback.print_exc()

        print(result)

        meaning_str = json.dumps(meaning)
        meaning_json = json.loads(meaning_str)
    

    def inputMeaning(self):
        verb = input('Give the verb meaning: ')
        adjective = input('Give the adjective meaning: ')
        noun = input('Give the noun meaning: ')
        adverb = input('Give the adverb meaning: ')
        others = input('Any other meaning: ')

        return (verb, adjective, noun, adverb, others)


    def processMeaning(self, meaning):
        #Remove all nonsense
        meaning_str = json.dumps(meaning)
        meaning_str = meaning_str.replace("`", "")
        meaning_str = meaning_str.replace("'", "")
        #meaning_str = meaning_str.replace("\"", "'")

        print(meaning_str)
        meaning_json = json.loads(meaning_str)

        noun = meaning_json.get('Noun')
        adjective = meaning_json.get('Adjective')
        adverb = meaning_json.get('Adverb')
        verb = meaning_json.get('Verb')
        others = ''

        return (noun, adjective, adverb, verb, others)
    

