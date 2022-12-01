#mainprogram

#importing the function file
import functions

#while loop to iterate the menu
while True:
    functions.main_menu()
    user_input = input("Choose an option from the above menu:")
    user_input = user_input.upper() #gives the user the ability to enter in any case
    if user_input == "ADD":
        functions.add_driver_function()
    elif user_input == "DDD":
        functions.delete_driver_function()
    elif user_input == "UDD":
        functions.update_driver_function()
    elif user_input == "VCT":
        functions.points_display_function()
    elif user_input == "SRR":
        functions.random_race_function()
    elif user_input == "VRL":
        functions.race_info_display_function()
    elif user_input == "STF":
        functions.save_data_function()
    elif user_input == "RFF":
        functions.load_data_function()
    elif user_input == "ESC":
        functions.exit_program_function()
    
