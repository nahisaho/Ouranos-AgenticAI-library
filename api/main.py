"""
FastAPI main application entry point.
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config import settings
from api.routers import prompts, categories, chat, agents, search

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown."""
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    
    # TODO: Initialize database connection
    # TODO: Run database migrations
    # TODO: Import prompts to database
    
    yield
    
    logger.info("Shutting down...")
    # TODO: Close database connection


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Interactive AI Prompt Platform inspired by NotebookLM",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "version": settings.APP_VERSION,
        "database": "connected",  # TODO: Check actual DB connection
    }


# Include routers
app.include_router(prompts.router, prefix="/api", tags=["prompts"])
app.include_router(categories.router, prefix="/api", tags=["categories"])
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(agents.router, prefix="/api", tags=["agents"])
app.include_router(search.router, prefix="/api", tags=["search"])


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "api.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD,
    )
