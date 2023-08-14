from pydantic import BaseModel

class RequestRegionList(BaseModel):
    region_name: str
    