from dataclasses import dataclass


@dataclass
class Manager:
    id: str
    firstname: str
    lastname: str
    email: str
    type: str
