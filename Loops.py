#For Loop  - predefined amount of repetitions 
#Ranges range(1,8) - produces 1, 2, 3, 4, 5, 6, 7
#for x in (range, string, list)

# Range range(x) gives int from 0 - x range(x,y,z) gives int from x - y in z interval

# for num in range(1,21):
# 	if num == 4 or num == 13:
# 		print(f"{num} is unlucky")
# 	elif num % 2 == 1:
# 		print(f"{num} is odd")
# 	elif num % 2 == 0:
# 		print(f"{num} is even")
# x = int(0)
# while x < 10:
# 	for y in range(x):
# 		print(":)",end = '');
# 	x = x+1
# 	print("\n")



# #######################Number Guesser#####################
# import random
# random_number = random.randint(1,10)
# playing = True
# keep_playing = True

# while playing == True:
# 	random_number = random.randint(1,10)
# 	guess = input("Guess a number between 1 and 10:")
# 	while int(guess) != random_number:
# 		if int(guess) > random_number:
# 			guess = input("{} is too high, guess again".format(guess))
# 		if int(guess) < random_number:
# 			guess = input("{} is too low, guess again".format(guess))
# 	keep_playing = input("You were right! Do you want to play again y/n:")
# 	if keep_playing == "y":
# 		playing = True
# 	elif keep_playing == "n":
# 		playing = False

# 	else:
# 		keep_playing = input("I didn't understand that, do you want to keep playing y/n")
