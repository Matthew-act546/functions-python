name = str(input("Enter your name: "))

print("Do you want to greet? [Y/N]")
respond = str(input())

def greet():
	print(f"WELCOME!!! {name} this is our app!")

while respond.lower() != 'y' or respond.lower() != 'n':
	
	if respond.lower() == 'y':
		greet()
		break
	elif respond.lower() == 'n':
		print(f"This is our app {name}!!!")
		break
	else:
		print("please try again")
	respond = str(input())
	