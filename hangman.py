import random


name = input("What is your name? ")
# Here the user is asked to enter the name first

print("welcome ! ", name)

words = ['kingking', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','fire', 'water', 'board', 'greek']


word = random.choice(words)


print("Guess the characters")

guesses = ''

turns = 12


while turns > 0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char)
		else:
			print("_")
			failed += 1
	if failed == 0:
		print("You Won the game")
		print("The word is: ", word)
		break
	guess = input("guess a character:")
	guesses += guess
	if guess not in word:

		turns -= 1
		print("Wrong")

		print("You have", + turns, 'more guesses')


		if turns == 0:
			print("You Loose")
