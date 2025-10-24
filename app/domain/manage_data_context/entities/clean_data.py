from abc import ABC, abstractmethod

class CleanData(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def clean(self,extracted_data): pass
