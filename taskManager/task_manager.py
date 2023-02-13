#***Import libraries and format date to UK***
import datetime                                         #import datetime library to access current date later in the program

today_wrong_format = datetime.date.today()
today = today_wrong_format.strftime("%d/%m/%Y")         #convert y/m/d to british d/m/y format


#***Define functions***
def reg_user():
    if username == "admin":                             #this option is only enabled for user "admin"
        print("New user registration:")
        new_username = input("Please enter a username for the new user: ")

        username_available = True                       #check new username against login details taken from text file
        for i in user_details:
            if i[0] == new_username:
                print("Username has already been registered. Please try again.")
                username_available = False
                break
        
        if username_available == True:
            new_password = input("Please enter a password for the new user: ")
            new_password_confirm = input("Please confirm the new password: ")
            #check that password confirmation matches password and append new user to text file if so
            if new_password == new_password_confirm:
                with open("user.txt", "a") as f:
                    f.write(f"\n{new_username}, {new_password}")   
                print("User registration successful.")            
            else:
                print("Passwords do not match. Please try again.")
    else:
        print("Only admins may register new users.")


def add_task():
    task_user = input("Please enter the username of the person responsible for this task: ")
    task_title = input("Please enter a title for this task: ")
    task_description = input("Please enter a description of this task: ")
    task_due = input("Please enter the date this task is due: ")
    
    #append new task to task doc with task defaulted to being incomplete
    with open("tasks.txt", "a") as f:
        f.write("\n")
        f.write(f"{task_user}, {task_title}, {task_description}, {task_due}, {today}, No")


def view_all():
    #list all tasks from doc in correct format
    with open("tasks.txt", "r+") as f:
        for line in f:
            arr = line.split(", ")              #strings split into lists for access to seperate inputs
            completed = arr[5].strip("\n")      #strip new line characters here as '\' not allowed inside an f-string
            print(f'''Task:                   {arr[1]}
Assigned to:            {arr[0]}
Date assigned:          {arr[4]}
Due date:               {arr[3]}
Task complete?          {completed}
Task description:
 {arr[2]}
''')


def view_mine():
    with open("tasks.txt", "r+") as f:
        #loop through tasks to check if they have been assigned to the user, print any that apply 
        #or let the user know if they have no tasks to complete
        printed = 0                                 #initialise count to determine whether to print fail message later
        my_tasks = []
        for line in f:
            arr = line.split(", ")
            completed = arr[5].strip("\n")          #strip new line characters here as '\' not allowed inside an f-string
            if arr[0] == username:
                my_tasks.append(arr)
                printed += 1
                print(f'''\
Task number {printed}:          {arr[1]}
Assigned to:            {arr[0]}
Date assigned:          {arr[4]}
Due date:               {arr[3]}
Task complete?          {completed}
Task description:
  {arr[2]}
''')
        if printed == 0:                                        #check count and print fail message if no tasks have been printed
            print("You have no tasks to complete.\n")
        
        else:
            #if user has any assigned tasks, check if they want to edit them
            task_selection = int(input("Select a task to edit or mark as complete (or enter '-1' to return to main menu): ")) 
            if task_selection > 0:                              #check a task was picked
                task_index = task_selection-1                   #adjust task number to find its index
                with open("tasks.txt", "r") as f:
                    task_list = f.readlines()                   #create iterable list of tasks

                task_complete = input(f"Would you like to mark task {task_selection} as complete? (Yes/No): ")
                if task_complete.lower() == "yes":                                   
                    complete_task = task_list[task_index].split(", ")
                    if complete_task[5] == "No\n":              #check for new line character to maintain formatting of text file
                        complete_task[5] = "Yes\n"
                    else:
                        complete_task[5] = "Yes"

                    task_list[task_index] = ", ".join(complete_task)
                    with open("task.txt", "w") as f:
                        f.writelines(task_list)
                
                #editing a task shouldn't be possible if the task has been marked as complete so editing is put after an 'else' statement
                else:     
                    #if user selects to edit the chosen task they are prompted to enter a new value and it is replaced                                      
                    edit_input = input(f"Would you like to edit task {task_selection}? (Yes/No) ")
                    if edit_input.lower() == "yes":
                        task_edit = task_list[task_index].split(", ")
                        allocation = input(f"Would you like to change the user that task {task_selection} is assigned to? ")
                        if allocation.lower() == "yes":
                            new_allocation = input("Please enter the username of the person you would like to reassign this task to: ")
                            task_edit[0] = new_allocation

                        change_date = input(f"Would you like to change the date that this task is due? (Yes/No) ")
                        if change_date.lower() == "yes":
                            new_date = input("Please enter the new due date for this task: ")
                            task_edit[3] = new_date

                        task_list[task_index] = ", ".join(task_edit)            #after edits the task file is rewritten with edited text
                        with open("tasks.txt", "w") as f:
                            f.writelines(task_list)


def generate_reports():
    task_list = []                                                      #instantiate and populate iterable task list
    with open("tasks.txt", "r") as f:                                   
        for line in f:
            task_list.append(line.split(", "))
    task_count = len(task_list)
    tasks_completed = 0
    tasks_incomplete = 0
    tasks_overdue = 0

    #code checks whether task has been completed and if not whether it is overdue
    for i in range(len(task_list)):
        if task_list[i][5] == "Yes" or task_list[i][5] == "Yes\n":
            tasks_completed += 1
        elif datetime.datetime.strptime(task_list[i][4], "%d %b %Y") < datetime.datetime.strptime(today, "%d/%m/%Y"):
            tasks_incomplete += 1
            tasks_overdue += 1
        else:
            tasks_incomplete += 1

    percentage_incomplete = (tasks_incomplete/task_count) * 100
    percentage_overdue = (tasks_overdue/task_count) * 100

    #generate text report
    with open("task_overview.txt", "w") as f:
        f.write(f"""Total number of tasks:      {task_count}
Completed tasks:            {tasks_completed}
Incomplete tasks:           {tasks_incomplete}
Overdue tasks:              {tasks_overdue}
Incomplete %:               {percentage_incomplete}%
Overdue %:                  {percentage_overdue}%""")
    

    user_count = len(user_details)
    
    with open("user_overview.txt", "w") as f:
        f.write(f"Total registered users:         {user_count}\n\n")
        
        for i in range(len(user_details)):
            current_user = user_details[i][0]
            assigned_tasks = 0
            tasks_completed = 0
            tasks_overdue = 0           

            #loop through list of users to calculate how many tasks are assigned to each, how many are complete and how many overdue
            for i in range(len(task_list)):
                if task_list[i][0] == current_user:
                    assigned_tasks += 1
                    if task_list[i][0] == "Yes" or task_list[i][0] == "Yes\n":
                        tasks_completed += 1
                    elif datetime.datetime.strptime(task_list[i][4], "%d %b %Y") < datetime.datetime.strptime(today, "%d/%m/%Y"):
                        tasks_overdue += 1

            #only perform calculations if user has any tasks, otherwise math errors are generated (dividing by 0)
            if assigned_tasks > 0:
                percentage_of_total = (assigned_tasks/task_count) * 100
                percentage_complete = (tasks_completed/assigned_tasks) * 100
                percentage_incomplete = 100 - percentage_complete
                percentage_overdue = (tasks_overdue/assigned_tasks) * 100
            
                #output depends on whether each user has any tasks assigned
                f.write(f"""User:                           {current_user}
Assigned tasks:                 {assigned_tasks}
Percentage of total tasks:      {percentage_of_total}%
Assigned tasks complete %:      {percentage_complete}%
Assigned tasks incomplete %:    {percentage_incomplete}%
Assigned tasks overdue %:       {percentage_overdue}%

""")
            
            else:
                f.write(f"""User:                           {current_user}
Assigned tasks:                 {assigned_tasks}
Percentage of total tasks:      0%

""")


def display_statistics():
    with open("tasks.txt", "r+") as f:              #loop through lines in task file, print total number of lines
        task_count = 0
        for line in f:
            task_count += 1
 
    with open("user.txt", "r+") as f:               #loop through lines in user file, print total number of users
        user_count = 0
        for line in f:
            user_count += 1 

    print(f"""Total tasks:        {task_count}
Total users:        {user_count}
""")


#***Software code***
user_details = []                                       #instantiate list to store login details from other document

with open("user.txt", "r+") as f:
    for line in f:
        users_seperate = line.split(", ")               #every line saved as a seperate subarray containing a username and its password
        user_details.append(users_seperate)

password_valid = False                              

#while loop will continuously ask for user login details until a correct combination is entered
while password_valid == False:                          
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    
    #loop compares user inputs to imported list of user credentials
    for i in range(0,len(user_details)):                
        if username == user_details[i][0] and password == user_details[i][1].strip("\n"):      #new line characters stripped from the end of each text file line 
            password_valid = True
                
    #declare failed logins
    if password_valid == False:        
        print("Invalid login credentials.")
            

while password_valid == True:                           #valid login presents user menu

    #alternate menu provided just for "admin" login
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()                                          #input converted to lowercase to make it non-case sensitive

#menu for all other users
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()

    if menu == "r":
        reg_user()            

    elif menu == "a":
        add_task()
        
    elif menu == "va":
        view_all()                

    elif menu == "vm":
        view_mine()

    elif menu == "gr" and username == "admin":          #option will only work if user is admin
        generate_reports()

    elif menu == "ds" and username == "admin":          #option will only work if user is admin
        display_statistics()

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


