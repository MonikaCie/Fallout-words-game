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
    lives = 5
    guess = ''
    while guess != word and lives > 0:
        guess = input('Guess a word => ').upper()
        count = 0
        for letter in word:
            if letter in guess:
                count = count + 1
        lives = lives - 1
        if guess == word:
            print(f'Congrats, the word was {word}')
        elif lives == 0:
            print(f'\nGAME OVER\nThe word was {word}')
        else:
            print(f'Your guess: {guess}\nNumber of matching letters: {count}\nLives left: {lives}\n')
        
        
    
    
    
fallout()
