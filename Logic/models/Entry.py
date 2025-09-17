from abc import ABC, abstractmethod

class Entry(ABC):
    @abstractmethod
    def get_amount(self):
        pass

    def __init__(self, description:str = "Unknown Description", amount:float = 0):
        self.description = description
        self.amount = amount
