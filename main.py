from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api.hotel import hotel_router
from api.index import app_router

app = FastAPI()

# Define the origins for CORS (update with your actual frontend URL)
origins = [
    "https://bizmedudev.bizflow.com",
    # Add other allowed origins here
]

# Apply the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hotel_router)
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)