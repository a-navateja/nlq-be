from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter(
    prefix="/testing", tags=["Testing"]
)

@router.get("/ping")
async def ping():
    """
    A simple endpoint to test if the API is working.
    """
    return {"message": "pong"}