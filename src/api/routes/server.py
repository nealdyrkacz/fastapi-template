from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def root():
    """Root endpoint."""
    return {
        "service": "FastApi Template App",
        "version": "1.0.0",
        "status": "running"
    }

@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "FastApi Template App",
        "version": "1.0.0"
    } 
