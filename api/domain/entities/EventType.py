from dataclasses import dataclass

@dataclass
class EventType:
    def __init__(self):
        self.id: int = 0
        self.typeName: str = ""
        self.typeImage: str = ""
        self.note: str = ""
        self.createdDate: str = ""
        self.typeIsPublic: bool = True
