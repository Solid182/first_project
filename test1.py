#Variation of programm with "While" cycle (to exit programm insert "PNH")
n=raw_input("What is your name: ")
i=1
while i != 5 and n != "PNH":
	print "Hello ", n
	i += 1
	n=raw_input("What is your name: ")


print "You enter", i, "names"
raw_input()
