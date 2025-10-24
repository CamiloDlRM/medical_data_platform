from fastapi import FastAPI
from app.interfaces.api.routes import router as dataframe_router
app = FastAPI()

app.include_router(dataframe_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


