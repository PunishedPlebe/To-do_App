from to_do_list import *
from task import Task
import csv
import os

#I need to created a file reader to check for a user inputted file name to re-create an old to-do list

def main():
    print("Welcome to your To-Do List!")
    print("Please enter the name of the save file or new file you wish to interact with.")
    print("DO NOT INCLUED THE FILE EXTENSION")
    intro_input = input("Name: ")

    pgr_dir = os.path.dirname(__file__) # returns the directory of of where this file sits
    file_path = "to_do_list_files" #file pathway of save files relative to main
    file_name = intro_input + ".csv" #name of file
    final_file_path = os.path.join(pgr_dir, file_path, file_name) # concatinates all the pieces of the dynamic file path to get the final path
    file = None # here we're declaring a file var which will hold a global instance of the file which makes up this to_do_list save file
    to_do = To_Do_List() # initalizes global to_do var which will be our active to-do list for this run

    if os.path.exists(final_file_path) == False: # if final_file_path doesn't exits
        file = open(final_file_path, "x") # we create the file
        file.close() # then we close the file for now
    else: #if it does exist
        file = open(final_file_path, "r", newline="") #we open the file in read mode and read the raw data igonoring \n formatters so we don't break the text before the csv gets a change to read it
        reader = csv.reader(file)# creates a reader object called reader that iterates through the file line by line starting at pointer which is aimed at he 0 index cause we opened the file in "r"(read) mode
        temp_holder = [] # local array var to hold each string of attribute value to be passed to the Task class creator to generate Task objects
        for line in reader: # for each line reader returns until reader hits the end of the file
            temp_holder.append(line) # local array adds a list of attribute values
        #print(temp_holder) #this is a test line to see if it was reading correctly
        for task_attr_val_lst in temp_holder: # for every list of attribute values in the temp_holder list
            id = int(task_attr_val_lst[0]) #we create and id var = index 0 of the list cast as an int(cause the task constructor needs an int for this value)
            descript = task_attr_val_lst[1]# we create a descript var = index 1 of the list
            date = task_attr_val_lst[2] # we create a date var = index 2
            if task_attr_val_lst[3] == "False": #we check if the str value of task_attr_val_lst is the word "False" cause we're reading from a text file
                comp = False # we set the comp var = to it's corresponding bool value cause the task constructor requires a bool there
            else: # if the str value isn't "False" (it could only be one of the two)
                comp = True # we set the bool value to True
            new_task = Task(id,descript,date,comp) # we create a new task object
            to_do.add_task(new_task) # we add that task object to the to_do object
    #print("this is a test to make sure Task objects were created and added to to_do properly") #test line
    #print(f"Active: {to_do.task_list}") #test line
    #print(f"Completed: {to_do.completed}")#test line
    #print(f"All Tasks: {to_do.all_tasks}")#test line


    running = True #Bool representing the state of the program
    while running: #infinite loop to keep program running until user input changes running state
        print("Welcome to your To-Do List!")
        print("-----------------------------")
        print("MENU")
        print("1: View Tasks")
        print("2: Add a Task")
        print("3: Delete a Task")
        print("4: Mark a Task as Completed")
        print("5: Exit")

        input_loop = True #creates a bool representing the running state of the loop
        user_input = None # creates a local variable to be filled with user input
        while input_loop: # infinite loop to ensure user inputs something
            try: # this block tests the user input to ensure valid input
                user_input = int(input("Enter a number to choose an action: ")) # prompts for user input and casts string input value to string value
                input_loop = False # breaks infinite input loop cause we got a valid input
            except ValueError: # catches Value error when anthing but a number is entered into the input field
                print("Input must be a numerical value. Try again.") #prints error message prompting user for valid input


        if user_input == 1:
            a,b,c = to_do.view_task_list()
            print("----------Active Tasklist-----------")
            for item in a:
                print(f"Task ID: {item.task_id} Description: {item.description} Due Date: {item.due_date}")
            print("----------Completed Tasklist-----------")
            for item in b:
                print(f"Task ID: {item.task_id} Description: {item.description} Due Date: {item.due_date}")
            print("----------All Tasks Tasklist-----------")
            for item in c:
                print(f"Task ID: {item.task_id} Description: {item.description} Due Date: {item.due_date} Completed: {item.completion_status}")


        if user_input == 5: #breaks running loop to close the program
            running = False




main()
