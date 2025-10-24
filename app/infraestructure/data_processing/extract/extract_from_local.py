from domain.manage_data_context.entities.extract_data import *
import os
import kagglehub
import pandas as pd
from typing import Optional

class ExtractFromUrlPath(ExtractData):

    def __init__(self):
        super().__init__()
    
    def extract(self, url_path:str, file_type:str, delimiter:str):
        validation_str=url_path.split(":")

        if len(validation_str) != 0:
            if validation_str[0] == "https":
                file_download = kagglehub.dataset_download(url_path)
                file_path = os.path.join(file_download, "diabetes.csv")
                return self.file_type(file_path,file_type,delimiter)
            else:
                return "Url is not secure"
        else:
            return self.file_type(file_path,file_type,delimiter)
    
    def file_type(self,file_path:str,file_type:str, delimiter: str):

        if (file_type == "csv"):
            df = pd.read_csv(file_path, sep=delimiter)
            
        elif (file_type == "tsv" and delimiter):
            df = pd.read_table(file_path, sep=delimiter)
            
        else:
            df = pd.read_table(file_path, sep=delimiter)

        return df