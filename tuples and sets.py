#tuples and sets

#Tuples - An ordered collection or grouping of items 
#	numbers = (1,2,3,4) - uses parens
#	immutable - cannot be changed
#	x = (1,2,3) if attempt to change gives TypeError
#	Tuples are faster than lists
#	Makes code safer from bugs
###########Tuple Methods############
#dict.items returns tuples
#count - returns amount of times value occurs in tuple
#returns index of given value in tuple - returns value error if value DNE


################################################

#Sets - like formal mathematical sets
#	Collection of data with no duplicate values
#	unordered
#	cannot access by index
# created by s = {1,2,3} or s = set({1,2,3})
# 1 in s - True
# iterate through values using a for loop
#################Set Methods#############################
#s.add(x) - adds x doesn't throw error if item already exists
#s.remove(x) removes x from set , throws key error if item doesn't exist
#s.discard(x) removes x but doesn't throw error
#s.copy() makes copy but not same memory
#s.clear() removes all data in set


#########Set Math##############
#set union  math_students | bio_students - joins two sets without duplicates
#set intersection math_students & bio_students - returns values present in both sets



#########Set Comprehension
######