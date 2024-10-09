from fastapi import FastAPI

from backend.app.api import hello_router

app = FastAPI()

# Include routers from endpoints
app.include_router(hello_router)
