import argparse
import json
from datetime import datetime

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
    priority = args.priority
    due_date = args.due_date

    task_id = len(tasks) + 1

    new_task = {
        'id':task_id,
        'task': task,
        'priority':priority,
        'done':False,
        'due_date':due_date,
    }

    tasks.append(new_task)

    save_task(tasks)

    print(f"Added task: {task} (Priority: {priority})")

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
    parser = argparse.ArgumentParser(exit_on_error=False)

    sub_parsers = parser.add_subparsers(dest="command")

    # add task command
    add_parser = sub_parsers.add_parser("add", help="Add a new task to the todo list")
    add_parser.add_argument("task", metavar="task", help="Description of the task.")
    add_parser.add_argument("-p","--priority", choices=["low","medium","high"], help="Choose the priority of a task")
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

if __name__== "__main__":
    main()