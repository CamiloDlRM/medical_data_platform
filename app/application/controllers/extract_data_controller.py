from typing import Optional
from app.interfaces.api.models.extract_data_model import ExtractDataModel
from app.application.use_case.process_medical_dataset import *

class ExtractDataController():

    def __init__(self, extract_data_model: ExtractDataModel):
        
        self.extract_data_model=extract_data_model
        
    
    def extract_data_urlpath_controller(self):
        extract_use_case=ExtractDataUsecase(self.extract_data_model.url_path
                                            ,self.extract_data_model.file_type
                                            ,self.extract_data_model.delimiter)
        
        return extract_use_case.extract_data_path_usecase_etl()
        

