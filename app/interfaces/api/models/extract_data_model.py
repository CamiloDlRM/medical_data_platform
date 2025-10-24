from pydantic import BaseModel

class ExtractDataModel(BaseModel):
    url_path:str 
    file_type:str 
    delimiter:str
    