from enum import Enum


class Type(str, Enum):
    unstarted = "unstarted"
    started = "started"
    done = "done"


class Name(str, Enum):
    unscheduled = "Unscheduled"
    ready_for_development = "Ready for Development"
    in_progress = "In Progress"
    completed_dev = "Completed-dev"
    stopped = "Stopped"


class Verb(str, Enum):
    start = "start"
    finish = "finish"
    unstart = "unstart"
    done = "done"







