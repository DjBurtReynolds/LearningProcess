#Inspired by the meme that says if you save a quarter every day for a year you get $9125
#You actually get 91.25 however I thought it would be interesting to find out exactly how much you'd save adding an additional quarter each day of the year 
#Through running the program you can see that you'd save a whopping $16698.75
#Inspiration: https://me.me/i/gbg-bucks-a-quarter-a-day-for-a-year-will-get-d4b8594e1cd140ec85df6ff28db49e0c
print(sum([x*.25 for x in range(1,366)])) #multiplys each number from 1 - 365 by .25 and puts it in a list

## additional way to add all elements in list
# while i < len(quarter):
# 	total = total + quarter[i]
	# i+=1
