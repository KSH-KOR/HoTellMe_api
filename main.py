from fastapi import FastAPI
import uvicorn

from api.hotel import hotel_router
from api.index import app_router

app = FastAPI()

app.include_router(hotel_router)
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)