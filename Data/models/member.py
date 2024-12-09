from dataclasses import dataclass


@dataclass
class Member:
    id: str
    firstname: str
    lastname: str
    email: str
    joined_date: str
