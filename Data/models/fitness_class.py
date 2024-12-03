from dataclasses import dataclass

from Data.models.manager import Manager


@dataclass
class FitnessClass:
    id: int
    class_name: str
    max_capacity: int
    current_capacity: int
    members: str
    trainer: Manager
    time: str
    date: str
    locality: str
    link: str
