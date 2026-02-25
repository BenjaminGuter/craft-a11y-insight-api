import os
from fastapi import FastAPI
from dotenv import load_dotenv
from datetime import datetime
from src.models import AuditRequest, AuditResponse, Issue


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

@app.post("/audit")
async def audit_endpoint(request: AuditRequest) -> AuditResponse:
    """
    Audit endpoint - scans URL for accessibility issues
    (Dummy implementation for testing)
    """
    # Create dummy test issue
    dummy_issue = Issue(
        type="missing-alt-text",
        description="Image missing alt attribute",
        impact="serious",
        element="img"
    )
    
    return AuditResponse(
        url=str(request.url),
        score=75,
        issues=[dummy_issue]
    )