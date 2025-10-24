from abc import ABC, abstractmethod

class ExtractData(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def extract(self,url_path:str,file_type:str, delimiter:str): pass

    @abstractmethod
    def file_type(self,url_path:str,file_type:str, delimiter:str): pass