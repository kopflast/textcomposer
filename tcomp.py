#!/usr/bin/python3

'''
Einen zufälligen Text aus einer vorgegebenen Menge an Worten und Satzzeichen generieren.
Der Markov-Text-Composer ist inspiration für diese Spielerei.

Die Textwurzel ist ein Text von Kurd Laßwitz, Bis zum Nullpunkt des Seins, 
Erzählung aus dem Jahre 2371 (1871)
https://www.projekt-gutenberg.org/lasswitz/nullpunk/chap001.html

https://en.wikipedia.org/wiki/Markov_chain
'A Markov chain or Markov process is a stochastic model describing a sequence of possible events
in which the probability of each event depends only on the state attained in the previous event.'

von kopflast 2022

'''

# Import the numpy module
import numpy as np

# graped text from Website as txt-file
textfile = 'lasswitz_text.txt'
#textfile = 'paul_adler_naemlich.txt'
lasswitz = open(textfile, encoding='utf8').read()

# split text in words, delete whitespace and leave signs
corpus = lasswitz.split()

# generate word-pairs
def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
pairs = make_pairs(corpus)

# create dictonary from word-pairs
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

def main():
    run = True;
    while run == True:
        # Random startpoint for the chain, first Letter Uppercase
        first_word = np.random.choice(corpus)
        while first_word.islower():
            first_word = np.random.choice(corpus)
        chain = [first_word]
        # Lenght of the result in words
        n_words = int(input('Wieviele Worte sollen in die Kette (Zahl bitte)? '))

        # generate chain
        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))
        print('\n Wortkette: \n')
        print(' '.join(chain))
        # Ask for repeat
        check = input('\nNochmal y/n? ').lower()
        if check == 'y':
            run = True
            print('\n------------------------------------\n')
        else:
            run = False 

# Start the loop
if __name__ == '__main__':
    main()
