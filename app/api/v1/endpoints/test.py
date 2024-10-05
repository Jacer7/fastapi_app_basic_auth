from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from enum import Enum

router = APIRouter()

class MCQ(BaseModel):
    test_type: str
    categories: List[str] 
    num_questions: int 


@router.post("/test")
def test(request: MCQ):
    return {
        "test_type": request.test_type, 
        "categories": request.categories,
        "num_questions": request.num_questions,
        "status": "success"
    }