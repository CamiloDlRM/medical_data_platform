from typing import Optional
from infraestructure.data_processing.extract.extract_from_local import *
from domain.manage_data_context.services.data_lifecycle import DataLifecycle 
class ExtractDataUsecase():

    def __init__(self, url_path:str, file_type:str, delimiter:str):
        self.url_path=url_path
        self.file_type=file_type
        self.delimiter=delimiter

    def extract_data_path_usecase_etl(self):

        extract_from_url=ExtractFromUrlPath()

        processing_data= DataLifecycle(extract_from_url)

        return processing_data.etl(self.url_path,self.file_type,self.delimiter)

        
        
        