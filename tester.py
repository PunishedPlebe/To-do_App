from task import *
from to_do_list import *

def tester():
    print("-------------TESTING Task Class------------------")
    try:
        task1 = Task(1,"this is a test task", "01/11/1998")
        print(f"The task ID is: {task1.task_id}, {task1.description}, Due Date: {task1.due_date}")
    except Exception as e:
        print(e)

    try:
        task2 = Task("1","this is a test task", "01/11/1998") #tests catch for non int in first parameter
        print(f"The task ID is: {task2.task_id}, {task2.description}, Due Date: {task2.due_date}")
    except Exception as e:
        print(e)

    try:
        task3 = Task(1,57, "01/11/1998") #tests catch for non str in second parameter
        print(f"The task ID is: {task3.task_id}, {task3.description}, Due Date: {task3.due_date}")
    except Exception as e:
        print(e)

    try:
        task4 = Task(1,"this is a test task", 201011) #tests catch for non str in third parameter
        print(f"The task ID is: {task4.task_id}, {task4.description}, Due Date: {task4.due_date}")
    except Exception as e:
        print(e)

    try:
        task5 = Task(1,"this is a test task", "12.11.2021") #tests catch for no / seperator
        print(f"The task ID is: {task5.task_id}, {task5.description}, Due Date: {task5.due_date}")
    except Exception as e:
        print(e)

    try:
        task6 = Task(1,"this is a test task", "12/11/21") #tests incorrect date format
        print(f"The task ID is: {task6.task_id}, {task6.description}, Due Date: {task6.due_date}")
    except Exception as e:
        print(e)

        try:
            task7 = Task(1,"this is a test task", "ap/11/1998") #tests non digit entries
            print(f"The task ID is: {task7.task_id}, {task7.description}, Due Date: {task7.due_date}")
        except Exception as e:
            print(e)
    print("-------------END------------------")

    print("-------------TESTING To_Do_List Class------------------")

    to_do1 = To_Do_List() # initializes a To_Do_List Object
    print(to_do1.task_list, to_do1.completed, to_do1.all_tasks) # Prints the contents of all it's attributes

    #Test 1 Standard Test input
    task8 = Task(1,"this is a test task1", "01/11/1998")
    task9 = Task(2,"this is a test task2", "01/11/1997")
    task10 = Task(3,"this is a test task3", "01/11/1996")

    #Test 2 Standard Adds Tasks test
    to_do1.add_task(task8)
    to_do1.add_task(task9)
    to_do1.add_task(task10)

    for item in to_do1.task_list: #Prints descriptions of each task object in to_do1 task_list attribute
        print(item.description)

    # Test 2 Standard Remove Tasks Test
    to_do1.del_task(task8)
    to_do1.del_task(task10)

    for item in to_do1.task_list: #Prints descriptions of each task object in to_do1 task_list attribute
        print(item.description)

    # Repopluates to_do1 for further testing
    to_do1.add_task(task8)
    to_do1.add_task(task10)





    print("-------------END------------------")

tester()
