"""
API router for chat/dialogue operations.
"""

from fastapi import APIRouter, HTTPException
from api.models import (
    SessionCreateRequest,
    SessionCreateResponse,
    SessionDetail,
    MessageCreateRequest,
    Message,
)

router = APIRouter()


@router.post("/chat/sessions")
async def create_session(request: SessionCreateRequest) -> SessionCreateResponse:
    """
    Create a new dialogue session.
    
    REQ-DIALOGUE-001: When a user clicks "Start Dialogue", create a new chat session
    """
    # TODO: Implement session creation in database
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/chat/sessions/{session_id}")
async def get_session(session_id: str) -> SessionDetail:
    """
    Get session details.
    
    REQ-DIALOGUE-005: GET /api/chat/sessions/{id} - Get session details
    """
    # TODO: Implement database query
    raise HTTPException(status_code=404, detail="Session not found")


@router.get("/chat/sessions/{session_id}/messages")
async def get_session_messages(
    session_id: str,
    limit: int = 50,
    offset: int = 0,
) -> list[Message]:
    """
    Get message history for a session.
    
    REQ-DIALOGUE-005: GET /api/chat/sessions/{id}/messages - Get message history
    """
    # TODO: Implement database query with pagination
    return []


@router.post("/chat/sessions/{session_id}/messages")
async def send_message(session_id: str, request: MessageCreateRequest) -> Message:
    """
    Send a message in a session and get AI response.
    
    REQ-DIALOGUE-003: When a user sends a message, invoke AI agent
    """
    # TODO: Implement message storage and AI invocation
    raise HTTPException(status_code=501, detail="Not implemented")


@router.delete("/chat/sessions/{session_id}")
async def delete_session(session_id: str):
    """
    Delete a session.
    
    REQ-DIALOGUE-005: DELETE /api/chat/sessions/{id} - Delete session
    """
    # TODO: Implement session deletion
    return {"status": "deleted"}
