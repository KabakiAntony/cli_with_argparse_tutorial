
# Building a CLI Application With Argparse

A Command-Line Interface (CLI) is a method of interacting with a computer program by entering text commands. It provides a way of controlling programs, executing tasks, and manipulating system resources through a terminal or command prompt. A CLI offers a powerful and efficient way of interacting with programs, with developers and advanced users preferring to use it.
To build programs that accept input through the command line, the Python library avails the `argparse` module. The module simplifies the process of building command-line interfaces by providing the functionality to define command-line arguments, parse arguments, validate the user input, and generate help messages.
In this tutorial, we will explore how to use the `argparse` module by building a ToDo application that will be operated through the Command-Line. This project will serve as an example of introducing the various concepts of `argparse` and demonstrating their practical use. Therefore, throughout the tutorial, we will build the application incrementally while exploring the different features of the `argparse` module.
The ToDo application will allow users to manage tasks, by providing commands to add tasks, view the task list, mark tasks as done, and delete tasks. 
The code examples used in this tutorial can be found in [this GitHub repository](https://github.com/KabakiAntony/cli_with_argparse_tutorial).

## Setting up the Environment

Setting up the environment for the ToDo CLI project will involve getting a number of things ready. Let’s look at what you need:
The first thing you need is to have Python installed. If you don’t have Python installed in your system, download it [here](https://www.python.org/downloads/) and select the version of Python that is appropriate for your operating system.
The next thing you need to do is create the project directory, you can create the directory in your  integrated development environment (IDE) or you can create it on the terminal using the following command:
```sh 
mkdir todo_cli
```
This will create a new directory named `todo_cli`.
With the project directory created, let’s set up a virtual environment. A virtual environment is an isolated Python environment where you can install packages for a given project without affecting the global Python installation. 
To create a virtual environment you are going to use the `virtualenv` package, this package, however, does not come with the standard Python library, you have to install it. To do that you are going to use the following command:
```sh
pip install virtualenv
```
Once the package has finished installing, you can now go ahead and create a virtual environment in the `todo_cli` project directory. You create a virtual environment using the following command:
```sh
virtualenv myenv
```
The above command will create a virtual environment called `myenv`.  To use the virtual environment you need to activate it. To activate the virtual environment you will use the following command on **Linux** or **macOS**:
```sh 
. myenv/bin/activate
```
If you are using a **Windows** operating system, you can activate the environment  using the following command:
```sh
. myenv\Scripts\activate
```
Once the virtual environment has been activated, you will now go ahead and create the Python module that will hold the CLI application. For simplicity, we will call it `todo_cli.py`, to create the module you can use your preferred IDE and create a new file or you could use the command line to create it on ** Linux** or **macOS** using the following command:
```sh
touch todo_cli.py
```
The above command will create a file named `todo_cli.py`.  With the environment ready, we will now go ahead and build the application starting with the basic of commands using `argparse`.

## Building the ToDo CLI Application

For a start, we will build an application that accepts just one command for adding a task to a list, this will be a good introduction to the `argparse` module. 
Let's see an example of how you could do that:
```python
#todo_cli.py
import argparse

def add_task(args, tasks):
	task = " ".join(args.add[1:]) # Exclude the first element (command name)

	task_id = len(tasks) + 1

	new_task = {
    	'id':task_id,
    	'task': task
	}

	tasks.append(new_task)

	print(f"Added task: {task}")


def main():
	tasks = []

	parser = argparse.ArgumentParser()
	parser.add_argument("add", nargs="+")
	args = parser.parse_args()

	if args.add:
    	add_task(args, tasks)


if __name__== "__main__":
	main()
```
In the above code sample, the first thing you do is import the `argparse` module, this will avail the various methods that you will use for handling and parsing command line arguments.
 Command-line arguments are arguments that are passed to a command-line program when it executes. They allow users to interact with the program thereby modifying the behavior of the program.  
Command line arguments can take various forms, they could be **options**, **flags**, and **values**. **Options** are used to enable or disable certain features or specify settings, for example in the above code you have the `add` option that will be used to specify that we want to add a new task to our list, **while** flags denote a boolean state of a given action, for example, you could have a delete option but because you want to confirm that for sure that a user wants to delete a certain task you could add two flags to the delete option something like `- y` for yes go ahead and delete and `- n` to show you don’t want to delete, and finally  **values** are the data or additional input required by the program, so, in this case, values will be tasks we will be adding to the task list.
Let’s look at the `add_todo()` function, the role of this function as its name suggests is for adding todos or tasks to the to-do list. It takes in two arguments which are `args` and `tasks`.  It then defines a `task` variable that extracts the task description from the arguments, assigns a unique ID to the task, adds it to the tasks list,  then finally prints to the console the task you have just added to the list.
The `main` function is the entry point to your application, it is called every time this module is run. It defines an empty list named `todos`, which will hold your tasks as you add them from the command line. The `main` function also defines a positional command ` add` for your application that accepts one or more values using `nargs=”+”`, which allows users to specify multiple words for the task description. Then it passes the parsed arguments to the `add_task()` function.
To run the application you will use the following commands:
```sh
python todo_cli.py add Write an article on argparse
```
This will add the task “Write an article on argparse” to the ToDo list and display the following confirmation message on the command line:
```sh
Added task: Write an article on argparse
```
Overall that example just shows the basic usage of the `argparse` module in creating a command line interface. It shows the basic workflow of using the `argparse` module which takes the following basic steps.
import the module:
```python
#todo_cli.py
import argparse
```
Create a parser object:
```python
#todo_cli.py
parser = argparse.ArgumentParser()
```
Add one or more arguments to the parser object:
```python
#todo_cli.py
parser.add_argument(“add”)
```
Parse the arguments and store them in a variable: 
```python
#todo_cli.py
args = parser.parse_args()
```
Finally use the parsed argument to carry out some action in your application.

## Subparsers and Subcommands

The way the application is set up you can only use the `add` command, however, in a ToDo CLI application you need to view tasks, and mark tasks as done or delete tasks, and to do that you need to add some more commands for those particular use cases. However, just adding new positional arguments will not work since `argparse` will need the arguments to be supplied when you run the application and this presents a challenge where you cannot use the `add` and `view` commands at the same time or even `add` and `delete` commands. To solve this `argparse` enables us to define sub-commands.
Therefore instead of our application having just one command, the `add` command we will create different individual commands denoting the actions that one can carry out in our application. These individual commands are known as **sub-commands** they present the user with a way of executing a specific action by specifying a command. So in our application, we will have commands for `add`, `view`, `remove`, and `done`. 
To create subcommands, the `argparse` module allows us to define subparsers. They are particularly useful when you want to handle different actions based on the command specified by the user. Each subparser will represent a distinct set of commands or functionality within our CLI application. To create a subparser we will use the `add_subparsers()` method that is availed by the `argparse` module.
Overall subparsers will allow you to organize and handle different sets of commands, while subcommands will represent the specific actions or tasks users can execute.
Let’s then update our application to handle different user actions:
```python
#todo_2_cli.py
import argparse
import json

TASKS_FILE = 'tasks.json'

def save_task(tasks):
	with open(TASKS_FILE, 'w') as file:
    		json.dump(tasks, file)

def read_tasks():
	try:
    	with open(TASKS_FILE, 'r') as file:
        		tasks = json.load(file)
	except FileNotFoundError:
    		tasks = []
    
	return tasks

def add_task(args):
	tasks = read_tasks()
	task = args.task
	task_id = len(tasks) + 1

	new_task = {
    	'id':task_id,
    	'task': task,
	}

	tasks.append(new_task)
	save_task(tasks)
	print(f"Added task: {task}")


def view_tasks():
	tasks = read_tasks()
	print("ToDo List:")
	for task in tasks:
    	print(f"Task {task['id']}: {task['task']}")

def main():
	parser = argparse.ArgumentParser()
	sub_parsers = parser.add_subparsers(dest="command")

	# add task command
	add_parser = sub_parsers.add_parser("add")
	add_parser.add_argument("task", metavar="task")

	# view tasks command
	sub_parsers.add_parser("view")

	args = parser.parse_args()

	if args.command == "add":
    		add_task(args)
	elif args.command == "view":
    	 	view_tasks()

if __name__== "__main__":
	main()
```
In this iteration of our application, we make some changes to improve the program, in addition to the `argparse` module we import the `json` module, which will avail various functions to allow us to work with JSON data. For us to be able to perform various actions on the data we need to persist it, this is because the list we used in the first iteration will only hold for the duration that the program is running. So every time the script is run with a different command it reinitializes the list making it empty in each run. 
After the `json` module import, we create a JSON  file that will hold our tasks. Then we define a couple of functions, the `save_task()` function which will save tasks to the JSON  file, and the `read_tasks()` function which will retrieve `tasks` from the file and return them to the calling function. 
After those two functions, we define the `add_task()` which will be responsible for adding a new task to the file, and  `view_tasks()` which will be responsible for retrieving all tasks from the list and displaying them for the user.
The `main()` function, which is the entry point of our program, is where we define a parser object. Once we have created a parser object we can now go ahead and create a subparser using the `add_subparsers()` method of the parser object. Something that you will want to take note of is that we have passed an optional parameter `dest` to the `add_subparsers()` method with the value “command”. This signifies that when a user enters a subcommand in the command line it will be stored in the `command` attribute this will be useful when evaluating what was passed in the command line so that the program can take an action depending on the selected command. While the `dest` parameter is optional and `argparse` can create a command based on the name of the sub-parser, however,  specifying `dest` provides more clarity and control in your code.
Once we have created the subparser object you now go ahead and make the various subparsers and subcommands. 
`add_parser = sub_parsers.add_parser(“add”)` creates a new parser object for the `add` subcommand. Since the `add` command takes in an argument, which is the description of the task that we want to add to the list, therefore, we go ahead and add it using the following line of code `add_parser.add_argument(“task”,  metavar=”task”)` and doing that defines a positional argument named “task” hence it will be provided directly on the command line after the `add` command. Notice that it has a `metavar` parameter with the value `task` this just specifies the name that will be displayed for the argument in help and error messages.
`sub_parsers.add_parser("view")`  adds the “view” subcommand to the CLI application. The view command at this point does not take any arguments, however, as we improve the project we will add some optional arguments to it.
The `if` and `elif` block just checks which command the user entered in the command line and calls the relevant functions.
Let’s  now run the script and provide the two different commands:
```sh
python todo_2_cli.py add “Write an article on argparse”
```
Running the application ad specifying the `add` command and giving it the `task` argument in the form of the string “Write an article on argparse”, appends the task to the file, and if the file is not available it is created.  The command also gives the following output which just notifies that everything worked correctly. 
Output:
```sh
Added task: Write an article on argparse
```
To view the tasks on the file we will now run the application and supply the `view` subcommand this way:
```sh
python todo_2_cli.py view
```
The above command will give the following output:
```sh
ToDo List:
Task 1: Write an article on argparse
```
With those few additions using sub-parser and subcommands allows us to add more functionality to the application. Giving the user the ability to control the program in different ways by supplying different commands and arguments.

## Error handling and Help Messages

As you add more functionality to the application, you will expect that from time to time users will sometimes use invalid arguments or sometimes they will supply commands with missing arguments. Therefore, your application needs to handle errors and also give helpful information showing users how to use the application and the commands available.
`argparse`, therefore, provides built-in support for error handling and help messages, they are very beneficial since they help users understand how to use the application correctly and provide meaningful feedback when an error occurs.
By default `argparse` generates help messages that describe the available commands and arguments based on the parsers and arguments that you define.  However, on top of the default help message that is provided by `argparse` you can add your own help messages as you create the commands, these help messages become the description of what the command does. Right now the way we have set up the commands they don’t have any help messages. We will look at how to add help messages to a command shortly.
To access help in `argparse you don’t need to set up any commands as they are provided out of the box using the following commands `-h` or `--help`. Therefore to access the help message, you will run the application with any of the two flags. Let’s see how:
```sh
python todo_2_cli.py -h 
```
This will give an output similar to the one below:
```sh
usage: todo_2_cli.py [-h] {add,view} ...
positional arguments:
  {add,view}
options:
  -h, --help  show this help message and exit

```
The help message shows that the application takes in one optional command `-h`  for help and two positional arguments `add` and `view`. However, it is not very descriptive of what the commands do. To change that you will add a `help` parameter with the value of the help message that you want to be displayed for the command on the interactive help.
Let’s see how you add help messages to the commands, by updating the application and adding the code below in the given sections:
```python
#todo_2_cli.py
# …
# add task command
add_parser = sub_parsers.add_parser("add", help="Add a new task to the todo list")
add_parser.add_argument("task", metavar="task")

# view tasks command
sub_parsers.add_parser("view", help="Lists all the tasks in your todo list")
# …
```
In the above code, we have added the `help` parameter to the `add_parser()` method of the command we want to display the help message for. Therefore accessing help again from the command line we will have a more informative help message. 
Let’s access help again:
```sh
python todo_2_cli.py -h 
```
Output:
```sh
usage: todo_2_cli.py [-h] {add,view} ...

positional arguments:
  {add,view}
	add   	This adds a new task to the todo list
	view  	This lists all the tasks in your todo list

options:
  -h, --help  show this help message and exit
```
The help messages now say what each command does in the application and this is now more informative. So adding help messages to your commands provides the user with more informative information on what any particular command does.
So far we have run the application and provided all arguments needed correctly, what if we run the application with the `add` subcommand and fai to provide the task, this will result in a missing arguments error, or run it with the `view` subcommand and provided some argument, well the application is going to throw some errors and just like the help messages. `argparse` provides error handling out of the box. So the two different scenarios will give an output showing what happened. 
Let’s see an example:
```sh
python todo_2_cli.py add
```
In the above example, we have not provided the expected argument of the task that is to be added to our list so the application is not going to work and we will get an error message output similar to the one below:
```sh
usage: todo_2_cli.py add [-h] task
todo_2_cli.py add: error: the following arguments are required: task
```
Let’s now run the application and supply the `view` command with an argument:
```sh
python todo_2_cli.py view “test”
```
This will also fail since the `view` subcommand does not take any arguments and it will give an output similar to the one below:
```sh
usage: todo_2_cli.py [-h] {add,view} ...
todo_2_cli.py: error: unrecognized arguments: test
```
Well, the two different scenarios give back error messages that are quite descriptive and informative showing exactly what caused the error, therefore, a user will be able to rectify what caused the error. This shows the ability of `argparse` being able to handle errors and give help messages out of the box. Making it a very powerful module for use in developing command-line applications.

## Choices in Command Line Arguments

More often than not when a user is writing down the tasks they want to do over a certain duration, the user will want to classify the tasks in terms of their priority, there could be some that need to be carried out as soon as possible and some you don’t have to fulfill immediately and therefore they will want this information captured as they save the tasks. 
So to capture tasks in terms of their priority on the command line calls for a way of choosing and this introduces us to the concept of choices in command line arguments. `argparse` provides us with a way of adding `choices` to the optional or positional commands.
In this application, we want to choose the priority of a task at the point we are adding it to the list, this means then that we will have to extend the functionality of the `add` subcommand and since sometimes we may not always want to choose the priority of a task. We will use an optional argument to the `add` subcommand. So if a user wants to assign a certain priority to a task they will use the `add` subcommand with the optional flag `--priority` and then they can choose between the given choices which in this case will be `[“low”, “medium”, “high”]`.
Let’s enhance the application to add choices to the `add` subcommand, therefore, update the following lines of code:
```python
#todo_2_cli.py
#... 
def add_task(args):
   #...
    priority = args.priority
    task_id = len(tasks) + 1

    new_task = {
        'id': task_id,
        'task': task,
        'priority': priority,
    }
   #...
    print(f"Added task: {task} (Priority: {priority})")
#...

def main():
	#...
	# add task command
	add_parser = sub_parsers.add_parser("add", help="Add a new task to the todo list")
	add_parser.add_argument("task", metavar="task")
	add_parser.add_argument("-p","--priority", choices=["low", "medium", "high"])
	#...
```
In this updated code, the `add_task()` function has been modified to include the `priority` argument (`args.priority`) in the `new_task` dictionary. When a task is added, the `priority` value will be saved along with the task information. The updated code also prints the task and its priority when displaying the “Added task” message.
By adding the `--priority` argument to the `add_parser` object and retrieving its value in the `add_task()` function, you can now associate the priority information with the task. 
Therefore, by utilizing choices in command-line arguments, you can enforce specific valid values for certain arguments and ensure that the user provides valid input based on the available choices. So if a user runs the script and provides the `add` command with the `--priority` argument, `argparse` will enforce that the value of `--priority` must be one of the specified choices. If the user provides an invalid value, `argparse` will raise an error and display the appropriate error message.
Let’s see an example of how we could use the `add` command with the `--priority` argument and supply one of the choices:
```sh 
python todo_2_cli.py add “Edit this article” –priority high
```
This will give the following output:
```sh
Added task: edit this article (Priority: high)
```
Overall you can see that using choices in our commands gives abilities to extend the functionality of your application, giving the user many different ways of using the application.

## Adding Advanced Command Line Arguments
Up to this point, the CLI only has the `add` and `view` commands, and it only takes commands and arguments using strings, if you wanted to supply the ID of a task you would need to supply arguments in integer form. Using `argparse` it is possible to specify the `type` of argument a command takes. 
Using the `type` parameter of the `add_argument()` method you can specify the type of argument you expect for any given command and this gives you the ability to define more advanced commands.
Let’s therefore, update our application in the following sections of code to add `mark` and `remove` commands that will take the ID of the task the user wishes to mark as done or remove from the list.
```python
# todo_2_cli.py
 # ...
def add_task(args):
	#...

	new_task = {
    	'id':task_id,
    	'task': task,
    	'priority':priority,
    	'done':False,
	}

	#...

def mark_task_done(args):
	tasks = read_tasks()
	task_id = args.task_id

	for task in tasks:
    		if task['id'] == task_id:
        	task['done'] = True
        	save_task(tasks)
        	print(f"Marked task {task_id} as done.")
        	return
	print(f"Task {task_id} not found.")
def remove_task(args):
	tasks = read_tasks()

	task_id = args.task_id

	for task in tasks:
    	if task['id'] == task_id:
        	tasks.remove(task)
        	save_task(tasks)
        	print(f"Removed task {task_id}.")
        	return

	print(f"Task {task_id} not found.")

def view_tasks():
	tasks = read_tasks()
	print("ToDo List:")
	for task in tasks:
    	print(f"Task {task['id']}: {task['task']}, Priority:{task['priority']}, Done:{task['done']}")
 
def main():
	#...

	# Mark task as done command
	mark_parser = sub_parsers.add_parser("done", help="Mark task as done")
	mark_parser.add_argument("task_id", type=int)

	# Remove task command
	remove_parser = sub_parsers.add_parser("remove", help="Remove task from list")
	remove_parser.add_argument("task_id", type=int)    

	args = parser.parse_args()

	if args.command == "add":
    		add_task(args)
	elif args.command == "view":
    		view_tasks()
	elif args.command == "remove":
    		remove_task(args)
	elif args.command == "done":
    		mark_task_done(args)

#...
```
In this updated code, two new commands have been added: `remove` and `done`. The `done` command is used to mark a task as done by specifying the task ID. The `remove` command is used to remove a task by specifying the task ID.
We have also updated the `add_task()` specifically the `new_task` dictionary in order to accommodate the `done` status of a task. We also update the `view_tasks()`  function so the print function will capture the priority and done status of a task.
Each new command has its own sub-parser object (`mark_parser`, `remove_parser`) created using `sub_parsers.add_parser()`.  The respective arguments (`task_id` in this case) are added to the sub-parser objects to capture the necessary input. This update also includes the `help` string for each command.
Therefore running the application with the corresponding command and arguments, the program will perform the desired action based on the provided input.
Let’s see an example of running the script with the remove command:
```sh
python todo_2_cli.py remove 1
```
Output:
```sh
Removed task 1.
```
That option just removes the task with an ID of 1. 
Overall you can add various advanced commands to your CLI application giving your users different ways of operating with the application.

## Enhancing the ToDo CLI APPlication

The Todo application is almost complete now but we could add little more functionality to make it more flexible for the users. To do this we could add options like due dates, we could also sort tasks with their due dates, and filter them according to their priority. While we have already encountered the optional arguments in the choices and command line arguments sections. 
This section will also extensively make use of the optional commands to give the application these advanced features like sorting and filtering.
Let’s then update our code in the following places to add sorting of tasks, filtering, and setting due dates on tasks:
```python
#todo_2_cli.py
#...

from datetime import datetime

#...

def add_task(args):
	#...
    
	due_date = args.due_date

	task_id = len(tasks) + 1

	new_task = {
    	'id':task_id,
    	'task': task,
    	'priority':priority,
    	'done':False,
    	'due_date':due_date,
	}

	#...


def view_tasks(args):
	tasks = read_tasks()

	if args.sort:
    		tasks.sort(key=lambda task: task['due_date'])

	print("ToDo List:")
	for task in tasks:
    	if args.filter:
        	if task['priority'] == args.filter:
            	print_task(task)
    	else:
        		print_task(task)

def print_task(task):
    	status= "Done" if task['done'] else "Not Done"
    	due_date=task['due_date'] if task['due_date'] else "N/A"

    	print(f"""
    	Task {task['id']}: {task['task']},
    	Priority:{task['priority']},
    	Done:{status},
    	Due Date: {due_date},
    	""")


def main():
	#...
    
	# add task command
	add_parser = sub_parsers.add_parser("add", help="Add a new task to the todo list")
	add_parser.add_argument("task", metavar="task", help="Description of the task.")
	add_parser.add_argument("-p","--priority",choices=["low","medium","high"], help="Choose the priority of a task")
	add_parser.add_argument("--due-date", help="Task due date (YYYY-MM-DD)")


	# view tasks command
	view_parser = sub_parsers.add_parser("view", help="Lists all the tasks in your todo list")
	view_parser.add_argument("--sort", action="store_true", help="Sort tasks by due date")
	view_parser.add_argument("--filter", choices=["low", "medium", "high"], help="Filter tasks by priority")

	# Mark task as done command
	mark_parser = sub_parsers.add_parser("done", help="Mark task as done")
	mark_parser.add_argument("task_id", type=int, help="The ID of the task")

	# Remove task command
	remove_parser = sub_parsers.add_parser("remove", help="Remove task from list")
	remove_parser.add_argument("task_id", type=int, help="The ID of the task")   

	args = parser.parse_args()

	if args.command == "add":
    		add_task(args)
	elif args.command == "view":
    		view_tasks(args)
	elif args.command == "remove":
    		remove_task(args)
	elif args.command == "done":
    		mark_task_done(args)

#...
```
In this updated code we have added an import for `datetime` this will allow us to work with dates that will be used to indicate a todo `due_date`. Therefore we have to update the `add_task()` function and create a `due_date` variable that will also be added to the `new_task` dictionary.
We have also updated the`view_tasks()` function so that it will take in an argument, in order for it to be able to sort and filter tasks if the argument is supplied with the `view` command. We have also created a  new `print_task()` function that will print our tasks in a nice format.
In the `main()` function, we have added the following options:
**Due Date**: The `add` command now accepts an optional `--due-date` argument, which allows setting a due date for the task. The due date should be provided in the format “YYYY-MM-DD”.
**Sorting**: The `view` command now supports a `--sort` option. When this option is specified, the tasks will be sorted by their due dates in ascending order. The `--sort` option takes no value.
**Filtering**: The `view` command now supports a `--filter` option which takes values from any of the following choices “low”, “medium”, and “high”. When this option is specified only tasks with specified choice will be displayed.
We have also added help messages for all the additional optional commands, however, the help messages for optional arguments are shown at the top level of the help command to view the help messages you will have to specify the command and then the help option. Let’s see an example where you want to display help for the `add` commands:
```sh
python todo_2_cli.py add --help 
```
Output:
```sh
usage: todo_2_cli.py add [-h] [-p {low,medium,high}] [--due-date DUE_DATE] task
positional arguments:
  task              	Description of the task.

options:
  -h, --help        	show this help message and exit
  -p {low,medium,high}, --priority {low,medium,high}
                    	Choose the priority of a task
  --due-date DUE_DATE   Task due date (YYYY-MM-DD)
```
The output shows the positional and optional arguments that the `add` command takes and what each does.
Those changes enhance our application giving the user more commands and options to work with giving them different ways to work with it. 
Let’s see an example of running the application with the newer features:
```sh
python todo_2_cli.py add "submit this article" --priority high --due-date 2023-05-20
```
This will give the following confirmation message:
```sh
Added task: submit this article (Priority: high)
```
Using the `view` command with the `--filter` option:
```sh
python todo_2_cli.py view --filter medium
```
This option will not return anything since there are no tasks marked with priority medium.

## Conclusion

In this tutorial, we covered the development of a ToDo CLI application using the `argparse` module. Here are the main points we discussed:

**Introduction to argparse**: We learned about the `argparse` module, which allows us to easily define and parse command-line arguments for our CLI application.
**Basic usage**: We explored the `basic` usage of argparse, including defining positional and optional arguments, parsing command-line arguments, and accessing the parsed values.
**Building the ToDo CLI**: We built a ToDo CLI application step by step, starting with defining the basic commands and their arguments, such as adding tasks and viewing tasks.
**Storing tasks**: We added functionality to store the tasks in a file using JSON serialization. This allowed us to persist the tasks between different runs of the application.
**Advanced command-line arguments**: We introduced advanced argument concepts, such as marking tasks as done and removing tasks. We implemented the parsing and handling of these advanced arguments using `argparse`.
**Error handling and help messages**: We discussed error handling and how to customize error messages for missing or invalid arguments. We also explored how to display help messages to provide guidance to users.
**Choices in command-line arguments**: We learned about the concept of choices in command-line arguments and how to enforce valid values using `argparse`. We applied this to the priority argument for tasks.
**Enhancing the ToDo CLI**: We enhanced the ToDo CLI by adding additional features like sorting tasks, filtering tasks, and setting due dates. We used `argparse` to define and handle these new features and options.

Throughout the tutorial, we provided code examples and explanations to help you understand the concepts and implement the features in your own CLI applications.

By following this tutorial, you should have gained a good understanding of how to develop command-line applications in Python using argparse and how to add various features and options to make your CLI applications more powerful and user-friendly.

