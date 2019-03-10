bingo = 18
answer = int(input("guess the number"))
while 1:
	if answer == bingo:
		break
	else:
		answer = int(input("guess again"))
print("cool.")