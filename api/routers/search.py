"""
API router for search operations.
"""

from fastapi import APIRouter
from api.models import PromptSearchRequest, PromptSummary

router = APIRouter()


@router.post("/prompts/search")
async def search_prompts(request: PromptSearchRequest) -> list[PromptSummary]:
    """
    Search prompts (full-text and optional vector search).
    
    REQ-SEARCH-001: Full-text search across prompts
    REQ-SEARCH-002: (Optional) Semantic vector search
    """
    # TODO: Implement full-text search
    # TODO: (Optional) Implement vector search if embeddings exist
    return []
