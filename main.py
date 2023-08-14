from fastapi import FastAPI
import uvicorn
import asyncio

from api.hotel import hotel_router
from api.index import app_router

app = FastAPI()

app.include_router(hotel_router)
app.include_router(app_router)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(uvicorn.run(app, host="0.0.0.0", port=8001))