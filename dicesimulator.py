from random import randint
ch = True

while(ch):
	n = input("Wanna Roll the die? (Y/N)")
	if(n=='Y'):
		x = randint(1,6)
		print(x)
	else:
		print("Ok ill take back the die.")
		ch=False
