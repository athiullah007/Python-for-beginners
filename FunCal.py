# This is a simple program for calculating basic arithmetic values
import numpy as np

def add(): # This function takes 2 values from the user for adding them
	n1 = float(input("Enter The First Number: ")) # This is where the user has to enter values for calculating purpose
	n2 = float(input("Enter The Second Number: "))
	print("the sum is\t",n1+n2)
	return


def sub(): # This function takes 2 values from the user for subtracting them
	n1 = float(input("Enter The First Number: ")) # This is where the user has to enter values for calculating purpose
	n2 = float(input("Enter The Second Number: "))
	print ("the diff is\t",n1-n2)
	return


def multiple(): # This function takes 2 values from the user for multiplying them
	n1 = float(input("Enter The First Number: ")) # This is where the user has to enter values for calculating purpose
	n2 = float(input("Enter The Second Number: "))
	print ("the prod is\t",n1* n2)
	return


def div(): # This function takes 2 values from the user for dividing them (The zero error is fixed)
	n1 = float(input("Enter The First Number: ")) # This is where the user has to enter values for calculating purpose
	n2 = float(input("Enter The Second Number: "))
	if n1==0 or n2==0:
		print("Can't divide by zero!")
	else:
		print ("the div is \t",n1/n2)
	return


def average(): # This function first asks the user to enter the total value and then calculates the average
	n1=int(input("Enter the number of elements to be inserted: "))
	n2=[]
	for i in range(0,n1):
		elem=float(input("Enter element: "))
		n2.append(elem)
	avg=sum(n2)/n1
	print("Average of elements in the list \t",round(avg,2))
	return

# This functions takes 1 value from the user other then Zero (0) to calculate its average
def squareRoot(): 
	number = float (input("Enter a number to find the square root : "))
	if number < 0:
		print("Please enter a valid number.")
	else:
		sq_root = np.sqrt(number)
		print("Square root is\t", sq_root)
	return
	

# This asks the user to enter the number for accessing the arithmetic operation they want to use
choice = int(input(" Press 1. for Addition\n Press 2. for Subtraction\n"
                   " Press 3. for Multiplication\n"" Press 4. for Division\n"
                   " Press 5. for Average\n Press 6. for Square Root \t")) 


if __name__ == '__main__': # This is the main function where everything related to average happens
	#n1 = float(input("Enter The First Number: ")) # This is where the user has to enter values for calculating purpose
	#n2 = float(input("Enter The Second Number: "))
	#number = float(input("Enter number to calculate sqrt\t: ")) # This is where the user has to enter values for calculating purpose

# We have all the conditions here. As it is mentioned at the very top to enter number for selecting Arithmetic Operations, this is where that number is called

	if choice == 1: # (1) calls the Addition Function
		add()

	elif choice == 2: # (2) calls the Subtraction Function
		sub()

	elif choice == 3: # (3) calls the Multiplication Function
		multiple()

	elif choice == 4: # (4) calls the Division Function
		div ()

	elif choice==5: # (5) Calls the Average Function
		average()

	elif choice == 6: # (6) calls the Square root function
		squareRoot()
	else: # Just in case if the user preses number other then from 1-6 , i.e 0,8,9 etc, it'll print that message
		print("Wrong Choice! ")






