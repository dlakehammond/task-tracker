"""Task data model."""

import json
from dataclasses import dataclass, asdict
from pathlib import Path

TASKS_FILE = Path.home() / ".task-tracker" / "tasks.json"


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE) as f:
        return [Task.from_dict(t) for t in json.load(f)]


def save_tasks(tasks):
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TASKS_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
