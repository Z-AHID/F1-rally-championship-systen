#function file

#defining a function to display the main menu
def main_menu():
    print(""" \u001b[33m
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
            d_age = input("\u001b[33mEnter the age of the driver:")
            d_age = int(d_age)
            break
        except ValueError:
            print("\u001b[31mInvalid Entry!!! PLease enter a number value!")

    d_team = input("Enter the team name of the driver:")
    d_car = input("Enter the name of the car:")

    while True:
        try:
            d_points = input("\u001b[33mEnter current points of the driver:")
            d_points = int(d_points)
            break
        except ValueError:
            print("\u001b[31mInvalid Entry!!! PLease enter a nu`mber value!")

    driver_details = [d_name, d_age, d_team, d_car, d_points]
    f = open("cso.txt","a+")
    z = str(driver_details)
    f.write(z+'\n')
    f.close()
    print(z)

    print("\u001b[32mDriver details has been added succesfully")



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

    print("\u001b[32mDriver details has been deleted successfully")




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
                    d_age = input("\u001b[33mEnter the age of the driver:")
                    d_age = int(d_age)
                    break
                except ValueError:
                    print("\u001b[31mInvalid Entry!!! PLease enter a number value!")
            d_team = input("Enter the driver's team:")
            d_car = input("Enter the name of the driver's car:")
            while True:
                try:
                    d_points = input("\u001b[33mEnter current points of the driver:")
                    d_points = int(d_points)
                    break
                except ValueError:
                    print("\u001b[31mInvalid Entry!!! PLease enter a number value!")
            d_details = [d_name,d_age,d_team,d_car,d_points]
            f1.write(str(d_details)+ "\n")
            print("\u001b[32mDriver details of driver", driver_name, "has been updated")



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

    #generating a random date
    day = random.randint(1,25)
    month = random.randint(1,12)
    year = random.randint(2022,2023)
    date = datetime.date(year,month,day)
    race_date = str(date)

    #generating a random location out of given locations
    locations = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]
    race_location = random.choice(locations)

    #getting drivers name and entering the race details to a text file
    csofile = open("cso.txt", "r")
    csofile_lines = csofile.readlines()

    for x in csofile_lines:
        split_records = x.replace("[", "").replace("]", "").replace("\"", "").replace("'", "").replace(" ", "").replace("\n", "").split(",")
        driver_name = split_records[0]
        race_details = [race_date, race_location, driver_name]
        str_racedetails = str(race_details)
        temprace = open("temprace.txt", "a+")
        temprace.write(str_racedetails + "\n")



#function6
#defining a function to display the races
def race_info_display_function():
    print("Display race details")




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

    print("\u001b[32mCurrent data has been successfully saved")




#function8
#defining a function to load current data from text file
def load_data_function():

    file = open("savefile.txt","r")
    lines  = file.readlines()
    for line in lines:
        print(line)




#function9
#defining a function to exit the the program
def exit_program_function():
    print("\u001b[32mProgram Exited")
    exit()