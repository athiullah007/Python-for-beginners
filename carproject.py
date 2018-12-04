def BuyCar(i): #This function helps you select the car to want to buy
    i=int (input(print(" What type of car do you want to buy?\n Press.1 For BMW\n."
                       " Press.2 For Rolls Royce\n. Press. 3 For Mercedes Benz\n")))
    if i==1: #Depending on the number pressed by the user, the statments will proceed i.e If the user presses 1. it will buy BMW and so on.
        print("Congrats You have successfully bought a Brand New BMW!")

    if i==2:
        print("Congrats you have successfully bought a Brand New Rolls Royce!")
    if i==3:
        print("Congrats you have successfully bought a Brand New Mercedes Benz!")
    else :
        print("Please enter valid number! ")
        return


def SellCar(i): #This function helps the user to sell their cars for the amount they want
    i=int (input( print("Which company is your car from?\n Press. 1 For Toyota Camery\n Press. 2 For Hilux 4x4\n"
                        " Press 3. For Ferrari\n Press 4. For any other different Company\n ")))
    if i==1: #If the user presses 1. it will go for the Toyota Camery and then it will ask the amount the user wants to sell for
       amount =float(input(print("Enter the amount you want to sell for : ")))
    print("Congrats! Your car will be sold for ",amount)
    if i==2:
        amoun=float  (input( print ("Enter the amount you want to sell for : ")))
        print("Congrats! Your car will be sold for ", amount)
    if i==3:
        amount= float (input (print ("Enter the amount you want to sell for: ")))
        print("Congrats! Your car will be sold for ", amount)
    if i>4 & i<1:
        print ("Please enter valid number! ")
        return

def RepairCar(i): #This function helps the user repair their cars
    i=int (input(print("What kind of repairing do you want?\n Press 1. For Repairing the Engine\n"
                       " Press.2 For Repairing the Headlights\n Press. 3 For Tuning Up Your Car\n")))
    if i==1:
        print ("The engine will be repaired soon!")
    if i==2:
        print ("The headlights will be repaired soon!")
    if i==3:
        print ("The car will be tuned up soon!")
    if i>=3 & i<=1:
        print ("Please enter valid number! ")
        return


def WreckCar(i): #This function wrecks the car
    i =int(input( print("Your Car will be wrecked up soon!")))
    return

if __name__ == '__main__': #This is Main. This is where the functions are called
    i=int (input(print("Hello! What would you like us to do?\n Press 1: For Buying a New Car\n"
                       " Press 2: For Sellng your Car\n"
                       " Press 3: For Repairing your Car\n Press 4: For Wrecking your Car \n ")))
    if i==1:
        BuyCar(i)

    if i==2:
        SellCar(i)

    if  i==3:
        RepairCar(i)

    if i==4:
        WreckCar(i)

    if i>=4 & i<=1:
        print ("Please enter valid number! ")

