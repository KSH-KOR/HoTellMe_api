import sys 
import os
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

app_router = APIRouter()

@app_router.get('/')
def home():
    return 'Welcome to Bizflow api service'