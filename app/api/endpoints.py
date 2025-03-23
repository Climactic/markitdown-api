from fastapi import APIRouter, Depends, UploadFile

from app.core.security import get_api_key
from app.models.markdown import ConversionResponse, HealthResponse
from app.services.markdown_service import convert_file_to_text

router = APIRouter()

@router.post("/convert", response_model=ConversionResponse, tags=["conversion"])
async def convert_markdown(
    file: UploadFile,
    authenticated: bool = Depends(get_api_key)
):
    """
    Convert a file to markdown
    
    - **file**: File to convert
    
    Returns the converted markdown
    """
    text = await convert_file_to_text(file)
    return {"result": text}

@router.get("/health", response_model=HealthResponse, tags=["system"])
async def health_check():
    """
    Health check endpoint
    
    Returns the status of the API
    """
    return {"status": "healthy"} 