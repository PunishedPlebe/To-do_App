from task import Task #imports task object class from task.py

class To_Do_List():
    def __init__(self): #initalizes the class by creating 3 seperate lists
        self.task_list = [] # active tasklist
        self.completed = [] # finished tasklist
        self.all_tasks =  [] # complete tasklist as in all of them

    def add_task (self, task): # adds a task object to active and complete tasklists
        if isinstance(task, Task) == False: # checks to make sure input is correct type
            raise Exception("You can only add Tasks to the to-do list") # throws error
        else:
            self.task_list.append(task) # adds task to active tasklist
            self.all_tasks.append(task) # adds task to complete tasklist

    def del_task(self, task): # removes task object from active tasklist
        if isinstance(task, Task) == False: # checks to make sure input is correct type
            raise Exception("You can only delete Tasks from the to-do list") #Throws error
        else:
            for item in self.task_list:  # loops through all tasks in active tasklist
                if item.task_id == task.task_id: # checks to see if current task object iteration's id value is equal to the passed task object's id value
                    self.task_list.remove(task) # removes task from active tasklist
                    self.all_tasks.remove(task)
                    break #breaks out of loop cause we found what we were looking for
            else:# for-else loop (phyton only) normally you'd create a found variable like a bool and check its status after the break with an if statement
                raise Exception("The task you are looking for is no longer/never was in the task list") # if we can't find it we throw an error to let the user know

    def view_task_list(self): # returns all the lists and their current values
        return self.task_list, self.completed, self.all_tasks

    def mark_as_comp(self, task): # Changes the status flag of task object and moves it to a list of finished tasks
        if isinstance(task, Task) == False: # checking to make sure input is correct type
            raise Exception("You can only delete Tasks from the to-do list") # throwing an error if it isn't
        for item in self.task_list: # loop thorugh each task in active tasklist
            if item.task_id == task.task_id: #if id's match between input and current task in loop
                item.completion_status = True # we update that tasks flag
                self.completed.append(self.task_list.pop(self.task_list.index(item))) # we add it to the finished tasklist by poping it off the active tasklist
                break # we break out of loop cause we changed what we need to change
        else: # for-else loop (phyton only) normally you'd create a found variable like a bool and check its status after the break with an if statement
            raise Exception("The task you are looking for is no longer/never was in the task list") # throw an error if we can't find it
        for item in self.all_tasks: # loop through all the task objects in all_tasks list
            if item.task_id == task.task_id: # compare ids for a matach
                item.completion_status = True # if they match change the completion_status flag of item
                break # found what we were looking for so we break out of the loop
