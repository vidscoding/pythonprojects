#Name: Vidhi Kadakia
#GitHub Username: vidscoding
#Date: 09/06/2022
#Description: Asks a user whether they want to log in or retrive data of a client. Then it asks which client they would like to it for.
#There are two functions "take" and "retrive" which login and retrive the data of a client. After they chose a client, they are asked "What you want to log
#Diet or Excercise". After you login the diet or excercise, it will display "Successfully logged in at date and time using the getdate function.


def getdate():
    """Returns the current database system data and time"""
    import datetime
    return datetime.datetime.now()

def take(client):
    """Logs info from the client. It first asks the user if they want to log in for
    food or excercise and then it asks the user for which client would they want to
    log in."""
    if client == 1:
        choice = int(input("Enter 1 for excercise and 2 for Food: "))

        if choice == 1:
            enter = input("Type Here\n")
            with open ("arjuna-ex.txt", "a") as see:
                see.write(str([str(getdate())]) + ":" + enter + "\n")
            print("Sucessfully logged in at", getdate())

        elif choice == 2:
            enter = input("Type here\n")
            with open ("arjuna-food.txt","a") as see:
                see.write(str([(getdate())])+ ":" + enter + "\n")
            print("Sucessfully logged in at", getdate())

    elif client == 2:
        choice = int(input("Enter 1 for excercise and 2 for Food: "))

        if choice == 1:
            enter = input("Type Here\n")
            with open("darren-ex.txt", "a") as see:
                see.write(str([str(getdate())]) + ":" + enter + "\n")
            print("Sucessfully logged in at", getdate())

        elif choice == 2:
            enter = input("Type here\n")
            with open("darren-food.txt", "a") as see:
                see.write(str([(getdate())]) + ":" + enter + "\n")
            print("Sucessfully logged in at", getdate())


    elif client == 3:
        choice = int(input("Enter 1 for excercise and 2 for Food: "))

        if choice == 1:
            enter = input("Type Here\n")
            with open("anirudh-ex.txt", "a") as see:
                see.write(str([str(getdate())]) + ":" + enter + "\n")
            print("Sucessfully logged in at", getdate())

        elif choice == 2:
            enter = input("Type here\n")
            with open("anirudh-food.txt", "a") as see:
                see.write(str([(getdate())]) + ":" + enter + "\n")
            print("Sucessfully logged in at", getdate())
    else:
        print("Please enter a valid input for (1 = Arjuna), (2 = Darren), (3 = Anirudh)")


def retrieve(client):
    """This function retrives info of a particular client and prints that on the console. """
    if client ==1 :
        choice = int(input("Enter 2 for excercise and 1 for food: "))
        if choice == 1:
            with open("arjuna-food.txt") as see:
                for food in see:
                    print(food, end="")
        elif choice == 2:
            with open ("arjuna-ex.txt") as see:
                for ex in see:
                    print(ex, end="")

    elif client == 2:
        choice = int(input("Enter 1 for excercise and 2 for food: "))
        if choice == 1:
            with open("darren-ex.txt") as see:
                for food in see:
                    print(food, end="")
        elif choice == 2:
            with open("darren-food.txt") as see:
                for ex in see:
                    print(ex, end="")
    elif client == 3:
        choice = int(input("Enter 1 for excercise and 2 for food: "))
        if choice == 1:
            with open("anirudh-ex.txt.txt") as see:
                for food in see:
                    print(food, end="")
        elif choice == 2:
            with open("anirudh-food.txt") as see:
                for ex in see:
                    print(ex, end="")

    else:
        print("Please enter a valid input for (1 = Arjuna), (2 = Darren), (3 = Anirudh)")


print("health management system: ")
update=int(input("Press 1 for log the value and 2 for retrieve: "))

if update==1:
    clients = int(input("Press 1 for Arjuna 2 for Darren 3 for Anirudh: "))
    take(clients)
else:
    clients= int(input("Press 1 for Arjuna 2 for Darren 3 for Anirudh: "))
    retrieve(clients)