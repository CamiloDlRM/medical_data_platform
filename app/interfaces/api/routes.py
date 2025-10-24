from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.controllers.extract_data_controller import ExtractDataController
from models.extract_data_model import ExtractDataModel
router= APIRouter()

@router.post("/etl")
def post_dataframe(extract_data_model: ExtractDataModel):
    extract_data_controller=ExtractDataController(extract_data_model)
    result= extract_data_controller.extract_data_urlpath_controller()
    return JSONResponse(content=result, status_code=200)