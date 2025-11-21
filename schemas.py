"""
Database Schemas for the Reusable Menstrual Products App

Each Pydantic model represents a collection in MongoDB.
Collection name is the lowercase of the class name.

Use these models to validate incoming data and to document your API.
"""

from pydantic import BaseModel, Field
from typing import Optional, List


class User(BaseModel):
    """Users collection schema (optional, for personalization)"""
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    city: Optional[str] = Field(None, description="City/Location")
    is_active: bool = Field(True, description="Whether user is active")


class Product(BaseModel):
    """Reusable menstrual product catalog"""
    name: str = Field(..., description="Product name")
    type: str = Field(..., description="Type: cup | pad | underwear | disc | washer")
    description: Optional[str] = Field(None, description="Short description")
    price: float = Field(..., ge=0, description="Price in USD")
    materials: List[str] = Field(default_factory=list, description="Primary materials")
    sizes: List[str] = Field(default_factory=list, description="Available sizes")
    absorbency: Optional[str] = Field(None, description="Absorbency level if applicable")
    image: Optional[str] = Field(None, description="Primary image URL")
    rating: Optional[float] = Field(None, ge=0, le=5, description="Average rating")
    sustainability_score: Optional[int] = Field(None, ge=0, le=100, description="Sustainability score 0-100")
    in_stock: bool = Field(True, description="Whether product is in stock")


class Article(BaseModel):
    """Educational content"""
    title: str
    excerpt: Optional[str] = None
    content: str
    cover_image: Optional[str] = None
    tags: List[str] = Field(default_factory=list)


class Impactentry(BaseModel):
    """User impact tracking entries"""
    user_id: Optional[str] = Field(None, description="User identifier if available")
    date: str = Field(..., description="ISO date e.g., 2025-01-15")
    products_used: List[str] = Field(default_factory=list, description="IDs or names of products used")
    cycles_tracked: int = Field(1, ge=1, description="Number of cycles represented")
    pads_diverted: Optional[int] = Field(None, ge=0, description="Disposable pads/tampons avoided")
    plastic_avoided_grams: Optional[float] = Field(None, ge=0, description="Estimated plastic avoided in grams")
    money_saved_usd: Optional[float] = Field(None, ge=0, description="Estimated money saved in USD")
