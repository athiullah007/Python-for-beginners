"""a program for buying, selling, repairing and wrecking a car """

#This function helps you select the car to want to buy
def buyCar(i):
	i = int(input(print("What type of car you want to buy? \n",
								"Press 1 for BMW\n",
								"Press 2 for Toyota\n",
								"Press 3 for Ferrari\n",
								"Press 4 for other\n")))
	if i==1:
		print("You bought BMW")
	if i==2:
		print("You bought Toyota")
	if i==3:
		print("You bought Mercedes")
	if i==4:
		print("You bought different")
	elif i<1 & i>4:
		print("Invalid purchase")
	return
	
#This function helps you select the car to want to sell
def sellCar(i):
	i = int(input(print("What type of car you want to sell? \n",
								"Press 1 for BMW\n",
								"Press 2 for Toyota\n",
								"Press 3 for Mecedes\n",
								"Press 4 for other\n")))
	if i==1:
		amount =float(input(print("Enter the amount you want to sell for : ")))
		print("You sold BMW", amount)
	if i==2:
		amount =float(input(print("Enter the amount you want to sell for : ")))
		print("You sold Toyota", amount)
	if i==3:
		amount =float(input(print("Enter the amount you want to sell for : ")))
		print("You sold Mercedes", amount)
	if i==4:
		amount =float(input(print("Enter the amount you want to sell for : ")))
		print("You sold different", amount)
	elif i<1 & i>4:
		print("Invalid purchase")
	return
	
#This function helps you select the car to want to repair
def repairCar(i):
	i = int(input(print("What type of car you want to repair? \n",
								"Press 1 for BMW\n",
								"Press 2 for Ferrari\n",
								"Press 3 for Mecedes\n",
								"Press 4 for other\n")))
	if i==1:
		print("You repair BMW")
	if i==2:
		print("You repair Toyota")
	if i==3:
		print("You repair Mercedes")
	if i==4:
		print("You repair different")
	elif i<1 & i>4:
		print("Invalid repair")
	return	
	
#This function helps you select the car to want to wreck
def wreckCar(i):
	print("Your car will be wrecked")
	
 #This is Main. This is where the functions are called
if __name__ == '__main__':
	i = int(input(print("How can I help you? \n",
								"Press 1 for buying\n",
								"Press 2 for selling\n",
								"Press 3 for repair\n",
								"Press 4 for wreck\n")))
	if i==1:
		buyCar(i)
		
	if i==2:
		sellCar(i)
		
	if i==3:
		repairCar(i)
		
	if i==4:
		wreckCar(i)
	elif i<1 & i>4:
		print("oops!")
	

		
