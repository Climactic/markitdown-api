from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from typing import Optional

from app.core.config import settings

# API key security scheme
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# Authentication dependency
async def get_api_key(api_key: Optional[str] = Depends(api_key_header)):
    """
    Validate API key from header.
    If API_KEY is not set in environment, authentication is disabled.
    """
    # If API_KEY is not set, authentication is disabled
    if not settings.API_KEY:
        return True
    
    # Validate API key
    if api_key and api_key == settings.API_KEY:
        return True
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API Key",
        headers={"WWW-Authenticate": "ApiKey"},
    ) 