import os
import random

TotalAttempts = 5
os.system('clear')
print('Hello what is your name?')

name = input()
os.system('clear')


print('Enter a number between 1 and 100')
randomNumber = random.randint(1, 100)
guess = int(input())


def keepPlaying(attempts):
    print('Want to keep playing? y/n')
    keepPlaying = input()
    if keepPlaying == 'y':
        attempts = 5
        makeGuess(attempts)
    else:
        print('Thanks for playing!')
        exit()


def makeGuess(attempts):
    if attempts == 0:
        print('You lose 😭')
        keepPlaying(attempts)
    else:
        guess2 = int(input())
        checkRange(guess2, attempts)

def playAgain(attempts):
    print('Play Again? y/n')
    playAgain = input()
    if playAgain == 'y':
        resetAttempts = 5
        newGuess = int(input())
        randomNumber = random.randint(1, 100)
        checkRange(newGuess , resetAttempts)

def compareGuess(guess, attempts):
    if guess == randomNumber:
        print('Congratulations ' + name + ' you won!')
        playAgain(attempts)
    elif guess > randomNumber:
        print('Too high')
        newAattempts = attempts - 1
        makeGuess(newAattempts)
    elif guess < randomNumber:
        print('Too low')
        newAattempts = attempts - 1
        makeGuess(newAattempts)

def checkRange(guess, attempts):
    if guess > 100:
        print('Way too high')
    elif guess < 1:
        print('Way too low')
    else:
        compareGuess(guess, attempts)




checkRange(guess, TotalAttempts)
