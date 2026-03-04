from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import register_routers


app = FastAPI(
    # title=settings.PROJECT_NAME,
    title="Natural Language Query API",
    openapi_url=f"/api/v1/openapi.json",
)

# Set all CORS enabled origins
origins = [
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


register_routers(app, api_prefix="/api/v1")