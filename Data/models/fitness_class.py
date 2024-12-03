from dataclasses import dataclass


@dataclass
class FitnessClass:
    id: int
    class_name: str
    max_capacity: int
    current_capacity: int
    members: str
    trainer_id: int
    time: str
    date: str
    locality: str
    link: str
