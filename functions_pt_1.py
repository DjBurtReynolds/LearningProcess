# # # ######Functions##########
# # # #def function_name ():
# # # 	#block of code

# # # def happy_bday (name):
# # # 	print("HBD 2 U")
# # # 	print("HBD 2 U")
# # # 	print(f"HBD Dear {name}")
# # # 	print("HBD 2 U")


# # # happy_bday()

# # # ######Return files from function#######
# # # # in order to get value out of function must use return keyword
# # # #pops function off of call stack # ends function

# # from random import random

# # def flip_coin():
# # 	#Gen random num 
# # 	num = random()
# # 	if num > 0.5:
# # 		return "Heads"
# # 	else:
# # 		return "Tails"
# # print(flip_coin())
# # print(flip_coin())
# # print(flip_coin())



# # def generate_evens():
# #     num_list=[]
# #     for num in range(1,50):
# #         if num %2 == 0:
# #             num_list.append(num)
# #     return num_list

# # print(generate_evens())

# ## adding parameters


# # def square(num): #squares input
# # 	return num **2

# # for x in range(1,101): #gives list of squares 1 - 100
# # 	print(square(x))

# # def multiply(x,y):
# # 	return x*y

# #give parameter names that are sensical and english

# #arguments vs parameter

# ##Parameter - variable in method definition (in definition)

# ##Argument - data passed into parameter (in execution)

# #Common Return Mistakes - having return statment within a loop
# 	#return removes from callstack
# 	#if returning in else you don't need the else statement 

# #default params
# 	#more readable examples
# 	#more defensive to errors
# def exponent(num, power=2):
# 	return num ** power

# print(exponent(5))
# print(exponent(2,3))

## If animal is "pig", it should return "oink". 
## If animal is "duck", it should return "quack".  
## If animal is "duck", it should return "quack".  
## If animal is "dog", it should return "woof"
## If animal is anything else, it should return "?"
## If no animal is specified, it should default to "dog"


# def speak(animal="dog"):
#     if animal == "pig":
#         return "oink"
#     elif animal == "duck":
#         return "quack"
#     elif animal == "cat":
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     return "?"

#Keyword arguments allows to specify in function call if you know the name of the param
#adds flexibility
#helps in passing dictionary to functions

######Scope#########
#LEGB
#Local
#Embedded
#Global
#Built-in


###Documenting functions
#Triple Double Quotes
#accessible with func.__doc__


