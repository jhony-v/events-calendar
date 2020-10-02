from dataclasses import dataclass

@dataclass
class EventPerson:
    def __init__(self):
        self.id: int = 0
        self.userId: str = ""
        self.eventId: str = ""
