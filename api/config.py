"""
Configuration management for Ouranos API.
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    APP_NAME: str = "Ouranos Interactive Platform"
    APP_VERSION: str = "2.0.0"
    DEBUG: bool = False
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = False
    
    # Database
    SURREAL_URL: str = "ws://localhost:8001/rpc"
    SURREAL_NAMESPACE: str = "ouranos"
    SURREAL_DATABASE: str = "prompts"
    SURREAL_USER: str = "root"
    SURREAL_PASS: str = "root"
    
    # Prompts Directory
    PROMPTS_DIR: str = "/app/prompts"
    
    # AI Providers
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    OLLAMA_URL: Optional[str] = "http://localhost:11434"
    DEFAULT_AI_PROVIDER: str = "openai"
    DEFAULT_AI_MODEL: str = "gpt-4"
    
    # Security
    APP_PASSWORD: Optional[str] = None  # Optional password protection
    SECRET_KEY: str = "change-me-in-production"
    
    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
