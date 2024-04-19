Burak757_floor_plan = [] # this is the floor plan of the plane which will be filled out to hold the elements of the plane floor plan given in the final project document, this is importatnt because the functions i will be making later such as one to book a seat will be working with this

for i in range (0,7):  # since there are seven rows this will be keeping track of weather it is A,B,C, Walkway, ect...
    if i == 0:
        seat = "A" # when it starts, i will be = 0 so seat will be set to "A", this will be used in the next for loop to describe which seat it is, this pattern will continue for the rest of the collums
    if i == 1:
        seat = "B"
    if i == 2:
        seat = "C"
    if i == 3:
        seat = "Walk way"
    if i == 4:
        seat = "D"
    if i == 5:
        seat = "E"
    if i == 6:
        seat = "F"
    for x in range (1,81): # since there are 80 rows this will get the seat number for each collum
        if i != 3: # since on the given floor plan they are all seats except for walkway (and storage) and walkway is all collum 3, this controls that and makes sure that it only assigns seat number and availability if its not the walkway
            if i > 3 and x == 77 or x == 78: # since on the given floor plan storage is only on collums "D","E","F" and at row 77 and 78 on each of these collum (because this makes each new collum start at 0 and end at 80) it will acurately assign storage to where it should be acording to the floor plan given on the final project document
                Burak757_floor_plan.append(["Storage", "Not bookable"]) # assigns the storage places
            else:
                Burak757_floor_plan.append([str(x) + seat,"free"]) # since this only exicutes if its not a walkway and not a storage place this will accuratly add the seats (sets them all to free initaily)
        else:
            Burak757_floor_plan.append([seat, "Not bookable"]) # this will assign the walkways



"""
# the following code is not needed but will help see that the above function works for grading purposes

# here is code that prints out the floor plan so you can see that the code above accurately prints out the floor plan given in the final project director

 for i in range (0,7): 
    z = i * 80 # since the plane has 7 rows of 80 this helps keep track of which row
    print("") # this helps format it so it prints out in a easier to read format
    for x in range (0,80):
        print(Burak757_floor_plan[z + x],end="") # this prints out each specific seat in each row
"""

def display_menu(): # menu function that prints out the menu and gets users choice of what he wants to do
    print("Menu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")
    choice = input("Please select an option (1-5): ")
    return choice # returns what the user wants to do

def check_availability(seat_choice): # checks availablity of seat
    seat_not_found = True # initalises seat not found to true initaily
    for x in Burak757_floor_plan: # goes through each seat in the floor plan
        if x[0] == seat_choice: # if the name of the seat is the same as the one the user is seaching for it will exixute the if statement
            print("seat is " + x[1]) # it will then print the seats availablity
            seat_not_found = False # it will then set seat not found to false because the seat was found
            break  # will break out of the for loop because seat was found and actions were taken already
    if seat_not_found: # will go through if the seat was not found
        print("there is no seat on the system named " + seat_choice + " (please use floor plan which is given on final project document if confused on which seat numbers there are)") # informs the user the seat they are searching for was entered incorectly or not on the system
        while True: # since seat was not found this segment will check if user wants to search again or return to the menu
            choice = input("would you like to search again (\"yes\" or \"no\"): ")
            if choice == "yes":
                seat_choice = input("Enter the seat that you are checking availability for (for example: 35B): ")  # asks user what seat they are looking for (following the flight floor plan given on the final project document
                check_availability(seat_choice) # will then go through the function again with the new seat choice
                break  # breaks so it doesnt continue to else statement after
            elif choice == "no":
                break # breaks out of while loop if user enters no, which will return to the menu
            else:
                print("Please enter either \"yes\" or \"no\"")

def book_seat(seat_choice):
    seat_not_found = True  # initalises seat not found to true initaily
    for x in Burak757_floor_plan:  # goes through each seat in the floor plan
        if x[0] == seat_choice:  # if the name of the seat is the same as the one the user is seaching for it will exicute the if statement
            if x[1] == "Booked" or x[1] == "Not bookable": # if the seat is already booked or not bookable it will inform the user
                print("sorry "  + seat_choice + " is " + x[1])
                seat_not_found = False  # it will then set seat not found to false because the seat was found even though it was booked or not bookable
                break # will break out of the for loop because seat was found and actions were taken already
            else: # this will go through if the seat was found and it is free
                x[1] = "Booked" # it will then set the seat to booked
                print("seat " + x[0] + " was booked")  # it will then inform the user that they sucessfuly booked the seat
                seat_not_found = False  # it will then set seat not found to false because the seat was found
                break  # will break out of the for loop because seat was found and actions were taken already
    if seat_not_found:  # will go through if the seat was not found
        print("there is no seat on the system named " + seat_choice + " (please use floor plan which is given on final project document if confused on which seat numbers there are)")  # informs the user the seat they are searching for was entered incorectly or not on the system
        while True:  # since seat was not found this segment will check if user wants to search again or return to the menu
            choice = input("would you like to search again (\"yes\" or \"no\"): ")
            if choice == "yes":
                seat_choice = input("Enter the seat that you are trying to book (for example: 35B): ")  # asks user what seat they are looking for (following the flight floor plan given on the final project document)
                book_seat(seat_choice) # will then go through the function again with the new seat choice
                break # breaks so it doesnt continue to else statement after
            elif choice == "no":
                break  # breaks out of while loop if user enters no, which will return to the menu
            else:
                print("Please enter either \"yes\" or \"no\"")

def free_seat(seat_choice):
    seat_not_found = True  # initalises seat not found to true initaily
    for x in Burak757_floor_plan:  # goes through each seat in the floor plan
        if x[0] == seat_choice:  # if the name of the seat is the same as the one the user is seaching for it will exicute the if statement
            if x[1] == "Booked":  # if the seat is booked it will free it and let the user know the seat has been freed
                x[1] = "free" # sets the seat to free
                print(seat_choice + " is now " + x[1])
                seat_not_found = False  # it will then set seat not found to false because the seat was found even though it was booked or not bookable
                break  # will break out of the for loop because seat was found and actions were taken already
            else:  # this will go through if the seat was found and it is free
                print("seat " + x[0] + " was already free")  # it will then inform the user that seat they tried to free was already free
                seat_not_found = False  # it will then set seat not found to false because the seat was found
                break  # will break out of the for loop because seat was found and actions were taken already
    if seat_not_found:  # will go through if the seat was not found
        print("there is no seat on the system named " + seat_choice + " (please use floor plan which is given on final project document if confused on which seat numbers there are)")  # informs the user the seat they are searching for was entered incorectly or not on the system
        while True:  # since seat was not found this segment will check if user wants to search again or return to the menu
            choice = input("would you like to search again (\"yes\" or \"no\"): ")
            if choice == "yes":
                seat_choice = input("Enter the seat that you are trying to free (for example: 35B): ")  # asks user what seat they are looking for (following the flight floor plan given on the final project document
                free_seat(seat_choice) # will then go through the function again with the new seat choice
                break  # breaks so it doesnt continue to else statement after
            elif choice == "no":
                break  # breaks out of while loop if user enters no, which will return to the menu
            else:
                print("Please enter either \"yes\" or \"no\"")

def show_booking_state():
    seats_booked = 0 # starts off at 0 seats booked
    print("the following seats have been booked: ") # starts the text layout
    for x in Burak757_floor_plan: # goes through each seat in the floor plan
        if x[1] == "Booked": # if it is booked it will print out the seats name and let the user know it was booked
            print(x[0] + " was booked")
            seats_booked += 1 # increases the number of seats booked by 1
    if seats_booked == 0: # if no seats were booked it will let the user know
        print("no seats have been booked which means the aircrafts total of 474 seats are still remaining")
    else:   # if there are seats booked it will tell the user the amount remaining
        print("there are currently " + str(474 - seats_booked) + " unbooked seats remaining")


while True: # will continue to go through this until user enters 5 in display_menu function in which case it will break
    user_choice = display_menu() # this will call the display menu function which will print out the menu and return what the user wants to do (either 1, 2, 3, 4 or 5)
    if user_choice == "1":
        seat_choice = input("Enter the seat that you are checking availability for (for example: 35B, use floorplan for seat names): ") # asks user what seat they are looking for (following the flight floor plan given on the final project document)
        check_availability(seat_choice)
    elif user_choice == "2":
        seat_choice = input("Enter the seat that you are trying to book (for example: 35B, use floorplan for seat names): ")  # asks user what seat they are trying to book (following the flight floor plan given on the final project document)
        book_seat(seat_choice)
    elif user_choice == "3":
        seat_choice = input("Enter the seat that you are trying to free (for example: 35B, use floorplan for seat names): ")  # asks user what seat they are trying to book (following the flight floor plan given on the final project document)
        free_seat(seat_choice)
    elif user_choice == "4":
        show_booking_state()
    elif user_choice == "5":
        print("Exiting program.")
        break # since he chose 5 to exit the program this will end the while loop which will stop the menu
    else:
        print("Invalid option, please choose a valid number (1-5).") # this will happen if the user prints anything other than the given choices (reminds user the inputs they should use)