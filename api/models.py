"""
Pydantic models for API request/response validation.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


# === Prompt Models ===

class PromptMetadata(BaseModel):
    """Prompt metadata from YAML front matter."""
    id: str
    category: str
    frameworks: list[str]
    dialogue_stages: int
    version: str
    tags: list[str]
    created: str
    updated: str


class PromptSummary(BaseModel):
    """Prompt summary for list views."""
    id: str
    title: str
    category: str
    language: str
    frameworks: list[str]
    dialogue_stages: int
    tags: list[str]
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class PromptDetail(PromptSummary):
    """Full prompt details including content."""
    content: str


class PromptSearchRequest(BaseModel):
    """Request for prompt search."""
    query: str = Field(..., min_length=3)
    category: Optional[str] = None
    language: Optional[str] = None
    frameworks: Optional[list[str]] = None
    limit: int = Field(20, ge=1, le=100)


# === Category Models ===

class CategorySummary(BaseModel):
    """Category summary."""
    slug: str
    name: dict[str, str]  # {"en": "Business Management", "ja": "ビジネス管理"}
    description: dict[str, str]
    prompt_count: int


class CategoryDetail(CategorySummary):
    """Full category details with prompts."""
    prompts: list[PromptSummary]


# === Chat/Dialogue Models ===

class SessionCreateRequest(BaseModel):
    """Request to create a new dialogue session."""
    prompt_id: str


class SessionCreateResponse(BaseModel):
    """Response with new session ID."""
    session_id: str
    prompt_id: str
    current_stage: int
    created_at: datetime


class MessageCreateRequest(BaseModel):
    """Request to send a message in a session."""
    content: str = Field(..., min_length=1)


class Message(BaseModel):
    """Chat message."""
    id: str
    session_id: str
    role: str  # "user" | "assistant"
    content: str
    stage: int
    created_at: datetime


class SessionDetail(BaseModel):
    """Full session details."""
    id: str
    prompt_id: str
    current_stage: int
    created_at: datetime
    updated_at: datetime
    messages: list[Message]


# === Agent Models ===

class AgentInvokeRequest(BaseModel):
    """Request to invoke an AI agent."""
    prompt_id: str
    user_message: str
    conversation_history: Optional[list[Message]] = None


class AgentInvokeResponse(BaseModel):
    """Response from AI agent."""
    response: str
    stage: int
    is_final: bool
    meta_prompt: Optional[str] = None  # Only set if is_final=True


# === Error Models ===

class ErrorResponse(BaseModel):
    """Error response."""
    error: str
    detail: Optional[str] = None


# === Health Models ===

class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    database: str
    timestamp: datetime
