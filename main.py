Burak757_floor_plan = [] # this is the floor plan of the plane which will be filled out to hold the elements of the plane floor plan given in the final project document, this is importatnt because the functions i will be making later such as one to book a seat will be working with this

for i in range (0,7):  # since there are seven rows this will be keeping track of weather it is A,B,C, Walkway, ect...
    if i == 0:
        seat = "A" # when it starts, i will be = 0 so seat will be set to "A", this will be used in the next for loop to describe which seat it is, this pattern will continue for the rest of the collums
    if i == 1:
        seat = "B"
    if i == 2:
        seat = "C"
    if i == 3:
        seat = "Walk way "
    if i == 4:
        seat = "D"
    if i == 5:
        seat = "E"
    if i == 6:
        seat = "F"
    for x in range (1,81): # since there are 80 rows this will get the seat number for each collum
        if i != 3: # since on the given floor plan they are all seats except for walkway (and storage) and walkway is all collum 3, this controls that and makes sure that it only assigns seat number and availability if its not the walkway
            if i > 3 and x == 77 or x == 78: # since on the given floor plan storage is only on collums "D","E","F" and at row 77 and 78 on each of these collum (because this makes each new collum start at 0 and end at 80) it will acurately assign storage to where it should be acording to the floor plan given on the final project document
                Burak757_floor_plan.append(("Storage", "Not bookable")) # assigns the storage places
            else:
                Burak757_floor_plan.append((str(x) + seat,"free")) # since this only exicutes if its not a walkway and not a storage place this will accuratly add the seats (sets them all to free initaily)
        else:
            Burak757_floor_plan.append((seat, "Not bookable")) # this will assign the walkways



"""
# the following code is not needed but will help see that the above function works for grading purposes

# here is code that prints out the floor plan so you can see that the code above accurately prints out the floor plan given in the final project director

 for i in range (0,7): 
    z = i * 80 # since the plane has 7 rows of 80 this helps keep track of which row
    print("") # this helps format it so it prints out in a easier to read format
    for x in range (0,80):
        print(Burak757_floor_plan[z + x],end="") # this prints out each specific seat in each row
"""