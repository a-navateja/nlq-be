from app.endpoints import (
    testing,  
)

def register_routers(app, api_prefix: str):
    """
    Register all routers with the FastAPI application.
    
    Args:
        app: FastAPI application instance
        api_prefix: API version prefix (e.g., /api/v1)
    """
    routers = [
        (testing.router, "Testing"),
    ]

    for router, tag in routers:
        app.include_router(router, prefix=api_prefix, tags=[tag]) 
 