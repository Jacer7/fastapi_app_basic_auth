from fastapi import APIRouter, Query, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from enum import Enum

from app.core.security import get_current_user, get_admin_user
from app.utils.read_excel import read_questions_from_xlsx, get_unique_test_types_and_categories
router = APIRouter()
test_types, categories = get_unique_test_types_and_categories()



def get_test_types():
    """Returns the list of unique test types from the Excel file 
    which will be shown as dropdown in the frontend
    """
    
    return test_types

def get_categories():
    """Returns the list of unique test types from the Excel file 
    which will be shown as dropdown in the frontend
    """
    return categories


class MCQRequest(BaseModel):
    test_type: str
    categories: List[str] 
    num_questions: int 

@router.post("/generate_mcqs")
def generate_mcqs(
    request: MCQRequest,  
    test_types: List[str] = Depends(get_test_types),  
    available_categories: List[str] = Depends(get_categories),
    user: dict = Depends(get_current_user)
):
    """
    Endpoint to generate MCQs based on test type, categories, and number of questions.
    The request body contains the test_type, categories, and num_questions.
    """

    # Validate test_type against dynamically loaded values
    if request.test_type not in test_types:
        raise HTTPException(status_code=400, detail=f"Invalid test_type. Available: {test_types}")

    # Validate categories against dynamically loaded values
    invalid_categories = [category for category in request.categories if category not in available_categories]
    if invalid_categories:
        raise HTTPException(status_code=400, detail=f"Invalid categories: {invalid_categories}. Available: {available_categories}")

    # Validate the number of questions
    if request.num_questions not in [5, 10, 20]:
        raise HTTPException(status_code=400, detail="Number of questions must be 5, 10, or 20")
    
    # Mock function to read questions based on input, replace with actual logic
    questions = read_questions_from_xlsx(request.test_type, request.categories, request.num_questions)
    
    return {"questions": questions, 
            "test_type": request.test_type, 
            "categories": request.categories,
            "num_questions": request.num_questions,
            "status": "success",
            "user": user["user_type"]}