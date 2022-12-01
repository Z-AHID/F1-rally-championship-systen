#function file

#defining a function to display the main menu
def main_menu():
    print("""
    1. Type  ADD  for adding driver details
    2. Type  DDD  for deleting
    3. Type  UDD  for updating driver details
    4. Type  VCT  for viewing the rally cross standings table
    5. Type  SRR  for stimulating a random race
    6. Type  VRL  for viewing race table sorted according to date
    7. Type  STF  to save the current data to a text file
    8. Type  RFF  to load data from the saved text file
    9. Type  ESC  to exit the program
    """)

#function1
#defining a function to add driver details
def add_driver_function():
    d_name = input("Enter the name of the driver:")

    while True:
        try:
            d_age = input("Enter the age of the driver:")
            d_age = int(d_age)
            break
        except ValueError:
            print("Invalid Entry!!! PLease enter a number value!")

    d_team = input("Enter the team name of the driver:")
    d_car = input("Enter the name of the car:")

    while True:
        try:
            d_points = input("Enter current points of the driver:")
            d_points = int(d_points)
            break
        except ValueError:
            print("Invalid Entry!!! PLease enter a number value!")

    driver_details = [d_name, d_age, d_team, d_car, d_points]
    f = open("cso.txt","a+")
    z = str(driver_details)
    f.write(z+'\n')
    f.close()
    print(z)

    print("Driver details has been added succesfully")



#function2
#defining a function to delete driver details
def delete_driver_function():
    driver_name = input("Enter name of driver to be deleted:")
    f = open("cso.txt", "r")
    lines = f.readlines()
    f.close()

    f1 = open("cso.txt", "w")
    for line in lines:
        x = line.replace("[", "").replace("]", "").replace("\"", "").replace(" ", "").replace("'", "").split(",")
        if driver_name != x[0]:
            f1.write(str(line))
    f1.close()

    print("Driver details has been deleted successfully")




#function 3
#defining a function to update driver details
def update_driver_function():
    driver_name = input("Enter name of driver to be updated:")
    
    f = open("cso.txt", "r")
    lines = f.readlines()
    f.close()

    f1 = open("cso.txt", "w")
    for line in lines:
        lined = line.replace("[", "").replace("]", "").replace("\"", "").replace("'", "").replace(" ", "").split(",")
        if driver_name != lined[0]:
            f1.write(str(line))
        elif driver_name == lined[0]:

            print("""            |Update the drivers details below| 
|If you do not want to update please re-enter the same record| 
                """)
            d_name = input("Enter the name of the driver:")
            while True:
                try:
                    d_age = input("Enter the age of the driver:")
                    d_age = int(d_age)
                    break
                except ValueError:
                    print("Invalid Entry!!! PLease enter a number value!")
            d_team = input("Enter the driver's team:")
            d_car = input("Enter the name of the driver's car:")
            while True:
                try:
                    d_points = input("Enter current points of the driver:")
                    d_points = int(d_points)
                    break
                except ValueError:
                    print("Invalid Entry!!! PLease enter a number value!")
            d_details = [d_name,d_age,d_team,d_car,d_points]
            f1.write(str(d_details)+ "\n")
            print("Driver details of driver", driver_name, "has been updated")



#function4
#Defining a function to display champions standing order
def points_display_function():
    file = open("cso.txt","r")
    score,dict1 = [],{}
    lines = file.readlines()

    for x in lines:
        lined = x.replace("[", "").replace("]", "").replace("\"", "").replace("'", "").replace(" ", "").replace("\n","").split(",")
        score.append(lined[4])
        d_details = lined[0:5]
        dict1[(lined[4])] = d_details
    score.sort(reverse=True)

    print("  Name","","    Age",""," Team","","  Car","","   Points")
    for j in score:
        descending = dict1.get(j)
        print(descending)
    file.close()


#function5
#defining a function to stimulate a random race
def random_race_function():
    import datetime
    import random

    # implemeting lists to store name,date,location and position seperately
    name_list = []
    date_list = []
    location_list = []
    position_list = []
    points_list = []

    # this list stores the above implemented list's elements as one whole list
    new_list = []

    # generating a random date
    day = random.randint(1, 25)
    month = random.randint(1, 12)
    year = random.randint(2022, 2023)
    date = datetime.date(year, month, day)
    race_date = str(date)

    # generating a random location out of given locations
    locations = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]
    race_location = random.choice(locations)

    # opening the file which contains champions standing order to read driver names
    csofile = open("cso.txt", "r")
    csofile_lines = csofile.readlines()
    racefile = open("racefile.txt", "a+")

    # reading and retreiving driver name from champion standing order file to be passed to a list
    for x in csofile_lines:
        split_records = x.replace("[", "").replace("]", "").replace("\"", "").replace("'", "").replace(" ", "").replace(
            "\n", "").split(",")
        driver_name = split_records[0]
        name_list.append(driver_name)

    # using while loop to generate position
    count = 1
    while count <= len(csofile_lines):
        position_list.append(count)
        if count == 1:
            points_list.append(10)
        elif count == 2:
            points_list.append(7)
        elif count == 3:
            points_list.append(5)
        else:
            points_list.append(0)
        count += 1

    # using z variable to increment the index value of the lists
    random.shuffle(name_list)

    racefile.write("_" * 21 + "\n")
    racefile.write("location---> "+race_location+"\n")
    racefile.write("Date---> "+race_date+"\n")
    racefile.write(""+"\n")
    racefile.write("Position "),racefile.write("Name "),racefile.write("Points"+"\n")
    z = 0
    while z < len(csofile_lines):
        new_list = [position_list[z + 0],name_list[z + 0],points_list[z + 0]]
        new_list_str = str(new_list)
        print(new_list_str)
        racefile.write(new_list_str + "\n")
        z += 1
    racefile.write("_"*21+"\n")
    csofile.close()
    racefile.close()


#function6
#defining a function to display the races
def race_info_display_function():
    file = open("racefile.txt","r")
    readline = file.readlines()

    print(readline)





#function7
#defining a function to save the current data to a text file
def save_data_function():
    file = open("cso.txt","r")
    file2 = open("savefile.txt","w+")
    title1 = "Name"
    title2 = "Age"
    title3 = "Team"
    title4 = "Car"
    title5 = "Points"
    headings = [title1, title2, title3, title4, title5]
    headings_str = str(headings)
    file2.write(headings_str + "\n")

    line = file.readlines()
    for i in line:
        file2.write(i)

    file.close()
    file2.close()

    print("Current data has been successfully saved")




#function8
#defining a function to load current data from text file
def load_data_function():
    file = open("savefile.txt","r")
    lines  = file.readlines()
    for line in lines:
        print(line)

    option = input("Do you want to continue (y/n):")
    if option == "y":
        main_menu()
        user_input = input("Choose an option from the above menu:")
        user_input = user_input.upper()  # gives the user the ability to enter in any case
        if user_input == "ADD":
            add_driver_function()
        elif user_input == "DDD":
            delete_driver_function()
        elif user_input == "UDD":
            update_driver_function()
        elif user_input == "VCT":
            display_function()
        elif user_input == "SRR":
            random_race_function()
        elif user_input == "VRL":
            race_info_display_function()
        elif user_input == "STF":
            save_data_function()
        elif user_input == "RFF":
            load_data_function()
        elif user_input == "ESC":
            exit_program_function()
    else:
        print("Program Exited")
        exit()




#function9
#defining a function to exit the the program
def exit_program_function():
    print("Program Exited")
    exit()