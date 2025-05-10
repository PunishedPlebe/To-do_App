class Task():
    def __init__ (self, task_id, description, due_date, completion_status=False): #Creates a task object taking an int, str, str as input to generate the object
        if isinstance(task_id, int) == False: #checking to make sure task_id variable is correct type
            raise Exception("must be an int")
        else:
            self.task_id = task_id

        if isinstance(description, str) == False: #checking to make sure description variable is correct type
            raise Exception("must be a string")
        else:
            self.description = description

        if isinstance(due_date, str) == False: #checking to make sure due_date variable is correct type
            raise Exception("must be a string")
        else: #checking to ensure proper date formatting of string
            if due_date.count("/") != 2: # checks if the date contains more or less of the required seperators
                raise Exception("date requries 2 / sperators between MM/DD/YYYY")
            elif len(due_date) != 10: #checks if the date contains the required number of character to be a date
                raise Exception("date must be properly formated MM/DD/YYYY") #not formated correctly if there are more than the expected number of characters; throws error
            else:
                holder = due_date.split("/") #creates a temporary list of the individual parts of the date string seperated by the "/"
                for item in holder:  #loops thorugh all the values in holder list
                    if item.isdigit() == False: #checks to make sure all character in each index of the list are numbers
                        raise Exception("Date must be property formated with numerical values MM/DD/YYYY") #if they aren't, date isn't formatted properly. throws exception
                else:
                    self.due_date = due_date # if we get this far without throwing an error the date is formated correctly and value is assinged to task attribute

        self.completion_status = completion_status # we have a default value of false but you can pass a value here, it's to catch on re-construction
    def mark_as_complete(self):
        self.completion_status = True

    def get_description(self):
        return self.description
