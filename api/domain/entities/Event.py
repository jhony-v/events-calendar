from dataclasses import dataclass

@dataclass
class Event:
    def __init__(self):
        self.id: int = 0
        self.createdByUserId: int = 0
        self.eventTypeId: int = 0
        self.eventTitle: str = ""
        self.eventDescription: str = ""
        self.eventImage: str = ""
        self.eventIsActive: bool = True
        self.startDate: str = ""
        self.endDate: str = ""
        self.createdDate: str = ""
        self.updatedDate: str = ""