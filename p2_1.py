import random

answer = random.randint(1,10)
temp = input("guess a number:")
guess = int(temp)
if guess != answer:
	while guess!=answer:
		if guess <answer:
			print("Too small!")
		else:
			print("Too big!")
		temp = input("guess a number:")
		guess = int(temp)
	print("Bingo!")
else:
	print("Bingo!")