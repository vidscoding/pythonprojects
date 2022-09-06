# Create a food log file for each client
# Create an exercise log file for each client.
# Ask the user whether they want to log or retrieve client data.
# Write a function that takes the user input of the client's name. After the client's name is entered, A message should display "What you want to log. Diet or Exercise"
# Use function

def getdate():
    import datetime
    return datetime.datetime.now()

def take(client):
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