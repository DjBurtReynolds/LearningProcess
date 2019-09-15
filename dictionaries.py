# limitations of list - work to store particular data
# dictionaries - key value pairs - C++ structs

cat ={
	"name" : "Hamilton",
	"age": 3,
	"isCute": True
}
  
dictionary = dict(name = "Aaron", age = 3.5)

#accessing value

cat["name"] # Hamilton
cat["thing"] #key_error 


#iterate overing a dict

for value in cat.values() #gets values
for key in cat.keys() #gets keys
for key, value in cat.items(): #gets item pairs
	print(key, items)

# in keyword only test for keys 
# in x.values() tests for values

#############dictionary methods ##################

#clear - empties dictionaries
#copy - makes copy of dictionary 
#fromkeys - called on empty dict passes in iterable collection														
#get - retrieves a key in an object and returns none if key does not exist
# pop - takes single argument - key and returns removed value
# popitems - remove random item from dictionary 
# update - add keyvalue pairs from one dictionary to another

#dictionary comprehension

#{ ___ : ___ for ___ in ___} basic comp
#{key:('pair output' if x 'logic' else 'pair output') for key in list }