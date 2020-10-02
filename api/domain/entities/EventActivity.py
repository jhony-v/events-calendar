from dataclasses import dataclass

@dataclass
class EventActivity:
    def __init__(self):
        self.id: int = 0
        self.eventId: int = 0
        self.title: str = ""
        self.activityImage : str = ""
        self.description: str = ""
        self.createdDate: str = ""
        self.activityIsCompleted: bool = False
