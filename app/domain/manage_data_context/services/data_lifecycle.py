from manage_data import *
from entities.extract_data import *
from entities.clean_data import *
from entities.load_data import *

class DataLifecycle(ManageData):

    def __init__(self,extract: ExtractData, clean: CleanData, load: LoadData):
        super().__init__()
        self.extract= extract
        self.clean=clean
        self.load=load
    
    def etl(self, url_path: str, file_type:str, delimiter:str):
        data_extracted= self.extract.extract(url_path,file_type,delimiter)
        data_cleaned=self.clean.clean(data_extracted)
        data_loaded=self.load.load(data_cleaned)
        
        return data_loaded

        

        