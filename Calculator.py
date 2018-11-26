def add( n1, n2):
    print(n1+n2)
    return


def sub(n1, n2):
    print (n1-n2)
    return


def multiple(n1, n2):
    print (n1* n2)
    return


def div(n1, n2):
    print (n1/n2)
    return

def avg (n1,n2):
	"""n = int(input("Enter the number of elements to be inserted: "))
	a = []
	for i in range(0, n):
        elem = int(input("Enter element: "))
        a.append(elem) """
	avg = (n1+n2)/2
	print"Average of ",n1, "and",n2, "is ",round(avg, 2)
	return
n1 = float(input("Enter The First Number: "))
n2 = float(input("Enter The Second Number: "))
print("1. Add")
print("2. Sub")
print("3. Multi")
print("4. Div")
print("5. Average")

choice = int(input("Enter the number you want: 1/2/3/4/5 \t"))
if choice == 1:
    add(n1, n2)
elif choice == 2:
    sub(n1, n2)
elif choice == 3:
    multiple(n1, n2)
elif choice == 4:
    div (n1, n2)
elif choice == 5:
    avg(n1,n2)
else:
    print("Wrong Choice! ")