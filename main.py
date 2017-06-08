import random

WORDS = ("Automatic machine", "pentagon", "druid", "diploma", "anegdot")

word = random.choice(WORDS)

text = []

i = 5

while i != 0:
	print('In a word ', len(word)," Letters")
	print("You ", i ," Attempts to guess the letter")
	choice = input("Enter the letter: ")
	if choice in word:
		print("Yes")
		text += choice
	else:
		print("No") 
	i -= 1

print("And now guess the word")
print("You guessed these letters here",text)


quest = input("\nTry to guess the source word  ")

while quest != word and quest != "":
	print("Unfortunately you are not right")
	quest = input("\nTry to guess the source word  ")

if quest == word:
	print('\nYou guessed right')

print('\nThanks for the game')
input('\n\n Press Enter to exit.')
