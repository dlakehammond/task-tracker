"""Utility functions for task display."""


def format_task(task):
    status = "x" if task.completed else " "
    return f"[{status}] {task.id}: {task.title}"


def next_id(tasks):
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1
