"""
API router for prompt operations.
"""

from fastapi import APIRouter, HTTPException
from api.models import PromptSummary, PromptDetail

router = APIRouter()


@router.get("/prompts")
async def list_prompts(
    category: str | None = None,
    language: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> list[PromptSummary]:
    """
    List all prompts with optional filtering.
    
    REQ-PROMPT-003: GET /api/prompts - List all prompts with pagination
    """
    # TODO: Implement database query
    return []


@router.get("/prompts/{prompt_id}")
async def get_prompt(prompt_id: str) -> PromptDetail:
    """
    Get a single prompt by ID.
    
    REQ-PROMPT-003: GET /api/prompts/{id} - Get single prompt by ID
    """
    # TODO: Implement database query
    raise HTTPException(status_code=404, detail="Prompt not found")


@router.get("/prompts/{prompt_id}/content")
async def get_prompt_content(prompt_id: str) -> dict:
    """
    Get full markdown content of a prompt.
    
    REQ-PROMPT-003: GET /api/prompts/{id}/content - Get full markdown content
    """
    # TODO: Implement database query and markdown file reading
    raise HTTPException(status_code=404, detail="Prompt not found")
