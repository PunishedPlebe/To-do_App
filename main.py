from to_do_list import *

#I need to created a file reader to check for a user inputted file name to re-create an old to-do list

def main():
    running = True #Bool representing the state of the program
    while running: #infinite loop to keep program running until user input changes running state
        print("Welcome to your To-Do List!")
        print("-----------------------------")
        print("MENU")
        print("1: View Active Tasks")
        print("2: View Completed Tasks")
        print("3: View All Tasks")
        print("4: Add a Task")
        print("5: Delete a Task")
        print("6: Mark a Task as Completed")
        print("7: Exit")

        input_loop = True #creates a bool representing the running state of the loop
        user_input = None # creates a local variable to be filled with user input
        while input_loop: # infinite loop to ensure user inputs something
            try: # this block tests the user input to ensure valid input
                user_input = int(input("Enter a number to choose an action: ")) # prompts for user input and casts string input value to string value
                input_loop = False # breaks infinite input loop cause we got a valid input
            except ValueError: # catches Value error when anthing but a number is entered into the input field
                print("Input must be a numerical value. Try again.") #prints error message prompting user for valid input

        if user_input == 7: #breaks running loop to close the program
            running = False




main()
