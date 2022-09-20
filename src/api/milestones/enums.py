from enum import Enum


class State(str, Enum):
    in_progress="in progress"
    done="done"
    to_do="to do"

