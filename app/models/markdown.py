from pydantic import BaseModel

class ConversionResponse(BaseModel):
    """
    Response model for file conversion endpoint
    """
    result: str

class HealthResponse(BaseModel):
    """
    Response model for health check endpoint
    """
    status: str