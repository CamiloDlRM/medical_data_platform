from abc import ABC, abstractmethod

class LoadData(ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def load(self,cleaned_data): pass