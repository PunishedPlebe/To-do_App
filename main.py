from to_do_list import *
from task import Task
import csv
import os
import time

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
        file.close()
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


        if user_input == 1: # if user selects view option
            a,b,c = to_do.view_task_list() # a,b,c var are initalized with task_list,completed,and all_tasks respectively
            print("----------Active Tasklist--------------")
            for item in a:
                print(f"Task ID: {item.task_id} Description: {item.description} Due Date: {item.due_date}")
            print("----------Completed Tasklist-----------")
            for item in b:
                print(f"Task ID: {item.task_id} Description: {item.description} Due Date: {item.due_date}")
            print("----------All Tasks Tasklist-----------")
            for item in c:
                print(f"Task ID: {item.task_id} Description: {item.description} Due Date: {item.due_date} Completed: {item.completion_status}")


        if user_input == 2: # if user selects add tasks
            active = True # loop break var
            while active: # infinite local loop, it will run til we decided we're done adding stuff
                add_input1 = input("Please Enter a Description of the New Task: ") #description input
                add_input2 = input("Please Enter a Due Date for the New Task: ")# due_date input
                largest_id = None #finding the largest id value
                id_array = [] #holder array for all the int value of all the task_id attributes
                for task in to_do.all_tasks: #for every task object in the all_tasks attribute
                    id_array.append(task.task_id) #add the task_id value to the holder array
                try:
                    largest_id = max(id_array) #largest_id = largest int value in the holder list
                    new_id = largest_id + 1 #new_id = largest_id + 1 to ensure a unique ID number for each new task we try to add to to-do
                except ValueError: # catch ValueError that is thrown if id_array is empty(like when we're working with a new To-Do List that has no previous entries)
                    new_id = 1 # if we don't have anything in there we default to id 1
                # print(largest_id)
                try:
                    new_task = Task(new_id,add_input1,add_input2) #we try to create a task object with the user input
                    to_do.add_task(new_task)# we try to add the task to the to-do object
                except Exception as e: # catch custom exceptions witten into classes to prevent bad data from being passed to obeject constructors
                    print(e) # print the custom error corresponding to where the bad data was

                checkout = True # loop break var
                while checkout: # infinite local loop for continuation selection
                    final_input = input("would you like to add another task? Y/N: ") #input for what to do
                    if final_input == "N" or final_input == "n": # if input is N or n we trip the break variables to end add
                        active = False
                        checkout = False
                    elif final_input == "Y" or final_input == "y": #if yes we just break the checkout loop and go about adding another task again
                        checkout = False
                    else:
                        print("that is not a valid input! \n") #anything other than expected input throws an error message and checkout loops again prompting for input again

        if user_input == 3: # if user selects delete tasks
            active = True
            while active:
                if len(to_do.all_tasks) > 0:# if there are tasks to delete
                    id_input = input("Enter the Task ID of the Task you wish to delete: ") #prompt user for task ID number
                    found = False # found flag
                    for task in to_do.all_tasks: # for each task in all_tasks
                        if task.task_id == int(id_input): #if the task ID number is equal to the user input
                            try:
                                to_do.del_task(task) #we try and delete the task from to-do
                                found = True
                            except Exception as e: #if we can't for some reason we catch with the custom exception
                                    print(e) #we print the custom error
                    if found == False: # if user input id number isn't in the list of tasks
                        print("Can't delete a task that isn't there") # print error message
                else: # if all_task is empty
                    print("To-Do List is now empty.\n Exiting to Main Menu...") #we notify the user the list is empty and that we're force quiting
                    time.sleep(2) #wait 2 seconds so user can actually read the message
                    break # break out of while active loop ending function

                checkout = True # loop break var
                while checkout: # infinite local loop for continuation selection
                    final_input = input("would you like to Delete another task? Y/N: ") #input for what to do
                    if final_input == "N" or final_input == "n": # if input is N or n we trip the break variables to end add
                        active = False
                        checkout = False
                    elif final_input == "Y" or final_input == "y": #if yes we just break the checkout loop and go about adding another task again
                        checkout = False
                    else:
                        print("that is not a valid input! \n") #anything other than expected input throws an error message and checkout loops again prompting for input again

        if user_input == 4:
            active = True
            while active:
                if len(to_do.task_list) > 0:# if there are active tasks
                    id_input = input("Enter the Task ID of the Task you wish to mark completed: ") #prompt user for task ID number
                    found = False # found flag
                    for task in to_do.task_list: # for each task in all_tasks
                        if task.task_id == int(id_input): #if the task ID number is equal to the user input
                            try:
                                to_do.mark_as_comp(task) #we try and delete the task from to-do
                                found = True
                            except Exception as e: #if we can't for some reason we catch with the custom exception
                                    print(e) #we print the custom error
                    if found == False: # if user input id number isn't in the list of tasks
                        print("Can't complete a task that isn't there") # print error message
                else: # if active_tasks is empty
                    print("You have no more active tasks\n Exiting to Main Menu...") #we notify the user the list is empty and that we're force quiting
                    time.sleep(2) #wait 2 seconds so user can actually read the message
                    break # break out of while active loop ending function

                checkout = True # loop break var
                while checkout: # infinite local loop for continuation selection
                    final_input = input("would you like to Complete another task? Y/N: ") #input for what to do
                    if final_input == "N" or final_input == "n": # if input is N or n we trip the break variables to end add
                        active = False
                        checkout = False
                    elif final_input == "Y" or final_input == "y": #if yes we just break the checkout loop and go about adding another task again
                        checkout = False
                    else:
                        print("that is not a valid input! \n") #anything other than expected input throws an error message and checkout loops again prompting for input again



        if user_input == 5: #breaks running loop to close the program
            #on close we write the contents of to-do to a csv file for potential future use
            file = open(final_file_path, "w", newline="") #we open the file in write mode
            writer = csv.writer(file) #we create a writer object that writes to file
            for task in to_do.all_tasks: #for all task objects in out lisk holding all Task objects
                row = ([task.task_id,task.description,task.due_date,task.completion_status]) # var which holds a single index list of all our attribute values
                writer.writerow(row) #writer object writes all the attribute values in the list to a row of the file with .csv formatting
            file.close() #we close the file cause we're done with it

            # if the file we're working out of is empty we delete the file
            if os.path.getsize(final_file_path) == 0: #if the size of final_file_path = 0
                os.remove(final_file_path) # we delete the file where it sits

            running = False


main()
