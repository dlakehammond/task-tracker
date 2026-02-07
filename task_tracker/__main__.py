"""CLI entry point for Task Tracker."""

import sys
from .models import Task, load_tasks, save_tasks
from .utils import format_task, next_id


def cmd_add(args):
    due = None
    if "--due" in args:
        idx = args.index("--due")
        due = args[idx + 1]
        args = args[:idx] + args[idx + 2:]
    title = " ".join(args)
    if not title:
        print("Error: task title required")
        sys.exit(1)
    tasks = load_tasks()
    task = Task(id=next_id(tasks), title=title, due=due)
    tasks.append(task)
    save_tasks(tasks)
    msg = f"Added task {task.id}: {task.title}"
    if task.due:
        msg += f" (due {task.due})"
    print(msg)


def cmd_list(args):
    tasks = load_tasks()
    for task in tasks:
        print(format_task(task))


def cmd_complete(args):
    if not args:
        print("Error: task ID required")
        sys.exit(1)
    task_id = int(args[0])
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            save_tasks(tasks)
            print(f"Completed task {task.id}: {task.title}")
            return
    print(f"Error: task {task_id} not found")
    sys.exit(1)


def cmd_remove(args):
    if not args:
        print("Error: task ID required")
        sys.exit(1)
    task_id = int(args[0])
    tasks = load_tasks()
    tasks = [t for t in tasks if t.id != task_id]
    save_tasks(tasks)
    print(f"Removed task {task_id}")


COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "complete": cmd_complete,
    "remove": cmd_remove,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m task_tracker <command> [args]")
        print(f"Commands: {', '.join(COMMANDS)}")
        sys.exit(1)

    command = sys.argv[1]
    if command not in COMMANDS:
        print(f"Unknown command: {command}")
        sys.exit(1)

    COMMANDS[command](sys.argv[2:])


main()
