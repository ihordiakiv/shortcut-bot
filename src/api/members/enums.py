from enum import Enum


class Role(str, Enum):
    member = "member"
    owner = "owner"
    admin = "admin"
