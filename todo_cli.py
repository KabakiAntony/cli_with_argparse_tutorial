import argparse

def add_task(args, tasks):
    task = args.task 

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
    parser.add_argument("task", nargs="+")
    args = parser.parse_args()

    if args.task:
        add_task(args, tasks)


if __name__== "__main__":
    main()