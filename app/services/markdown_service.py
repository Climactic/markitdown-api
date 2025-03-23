import logging
from markitdown import MarkItDown
from fastapi import UploadFile, HTTPException, status
import io

from app.core.config import settings

# Configure logging
logger = logging.getLogger(__name__)

# Initialize MarkItDown
if settings.OPENAI_API_KEY:
    from openai import OpenAI
    llm_client = OpenAI(api_key=settings.OPENAI_API_KEY, base_url=settings.OPENAI_API_BASE)
    md = MarkItDown(llm_client=llm_client, llm_model=settings.OPENAI_MODEL)
else:
    md = MarkItDown()

async def convert_file_to_text(file: UploadFile) -> str:
    """
    Convert uploaded file to markdown

    Args:
        file: The uploaded file
        
    Returns:
        The extracted text content
        
    Raises:
        HTTPException: If there's an error processing the file
    """
    try:
        # Read the file content
        content = await file.read()
        
        # Create a file-like object from the content
        file_stream = io.BytesIO(content)
        
        # Convert the file stream to markdown
        result = md.convert_stream(file_stream)
        text = result.text_content
        
        return text
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing file: {str(e)}",
        ) 