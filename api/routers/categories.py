"""
API router for category operations.
"""

from fastapi import APIRouter, HTTPException
from api.models import CategorySummary, CategoryDetail

router = APIRouter()


@router.get("/categories")
async def list_categories() -> list[CategorySummary]:
    """
    List all categories.
    
    REQ-CAT-002: GET /api/categories - List all categories
    """
    # TODO: Implement database query
    return []


@router.get("/categories/{slug}")
async def get_category(slug: str) -> CategoryDetail:
    """
    Get category details.
    
    REQ-CAT-002: GET /api/categories/{slug} - Get category details
    """
    # TODO: Implement database query
    raise HTTPException(status_code=404, detail="Category not found")


@router.get("/categories/{slug}/prompts")
async def get_category_prompts(slug: str):
    """
    Get prompts in a category.
    
    REQ-CAT-002: GET /api/categories/{slug}/prompts - Get prompts in category
    """
    # TODO: Implement database query
    return []
