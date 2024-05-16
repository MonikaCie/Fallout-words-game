import random
from words import words

randomWords = []

def generateRandomWords():
    while len(randomWords)<10:
        randomWord = random.choice(words)
        randomWords.append(randomWord)

generateRandomWords()

word = random.choice(randomWords).upper()

print('Words:', '  '.join(randomWords).upper())

def fallout():
    print(word)
    guess = input('Guess a word => ').upper()
    count = 0
    for letter in word:
        if letter in guess:
            count = count + 1
    print(guess)
    print(count)
    
    
fallout()
