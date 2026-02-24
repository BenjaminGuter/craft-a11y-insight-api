import os
from fastapi import FastAPI
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

app = FastAPI(title = os.getenv("APP_NAME", "A11y-Insights"), version = os.getenv("APP_VERSION", "0.1.0"))

@app.get("/")
async def root() -> dict:
    """
    Root endpoint - Welcome message
    """
    return {
        "message": "Welcome to A11y-Insight API",
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "docs": "/docs",
    }

@app.get("/status")
async def health_check() -> dict:
    """
    Health check endpoint for monitoring
    
    Returns server status, version, and timestamp
    """
    return {
        "status": "healthy",
        "service": os.getenv("APP_NAME","A11y-Insights" ),
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "timestamp": datetime.now().isoformat(),
    }