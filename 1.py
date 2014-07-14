print 'Yebin Choi'

total = 0
for x in range(51):
	total += x
print total

year=[1900,2000,2014,2015,2016]

for y in year:
	if (y%4 == 0 and y%100 != 100) or y%400 == 0:	
		print y

for x in range(6):
	print "*" * x

for x in range(2,10):
	for y in range(1,10):

		print x ,"*" , y , "=" , x*y


import random 
a = range(46)
b = 6

list1 = random.sample(a,b)
print list1



textfile = open("mess.txt","r")

content = textfile.read()
textfile.close()

total=''
for c in content:
 	if c.isalpha():
 		print c,
		total += total
 			
