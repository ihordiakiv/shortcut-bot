from enum import Enum


class StoryType(str, Enum):
    feature = "feature"
    bug = "bug"
    chore = "chore"
