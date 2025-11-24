"""
API router for AI agent operations.
"""

from fastapi import APIRouter, HTTPException
from api.models import AgentInvokeRequest, AgentInvokeResponse

router = APIRouter()


@router.post("/agents/{prompt_id}/invoke")
async def invoke_agent(
    prompt_id: str,
    request: AgentInvokeRequest,
) -> AgentInvokeResponse:
    """
    Invoke AI agent with a prompt (non-streaming).
    
    REQ-AGENT-003: POST /api/agents/{promptId}/invoke - Invoke agent
    """
    # TODO: Implement AI agent invocation
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/agents/{prompt_id}/stream")
async def stream_agent(prompt_id: str, request: AgentInvokeRequest):
    """
    Stream AI agent responses (SSE).
    
    REQ-AGENT-003: POST /api/agents/{promptId}/stream - Stream agent responses
    """
    # TODO: Implement streaming with Server-Sent Events
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/agents/{prompt_id}/stages")
async def get_agent_stages(prompt_id: str):
    """
    Get dialogue stages for a prompt.
    
    REQ-AGENT-003: GET /api/agents/{promptId}/stages - Get dialogue stages
    """
    # TODO: Implement stage information retrieval
    return []
