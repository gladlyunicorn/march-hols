import random

numberofGuesses = 0
number = random.randint(1,100)



print("I'm thinking of a number between 1-100. You have 7 guesses.")

while numberofGuesses < 7:
  guess = raw_input(" guess ")
  guess = int(guess)

  numberofGuesses = numberofGuesses + 1;
  guessesLeft = 7 - numberofGuesses;

  if guess < number:
    guessesLeft=str(guessesLeft)
    print(" too low! ")

  if guess > number:
    guessesLeft=str(guessesLeft)
    print(" too high! ")

  if guess==number:
    break

if guess==number:
  numberofGuesses=str(numberofGuesses)
  print("You guessed it! What are the odds??")

if guess!=number:
  number=str(number)
  print("Sorry, you didn't guess it in 7 tries! You lose.")