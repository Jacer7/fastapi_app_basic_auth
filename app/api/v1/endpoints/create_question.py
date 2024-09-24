from fastapi import APIRouter, Query, HTTPException, Depends
from app.core.security import get_admin_user
from app.utils.update_excel import append_question_to_excel
from pydantic import BaseModel
from typing import Optional
router = APIRouter()

# Define Pydantic model for creating a new question
class QuestionCreate(BaseModel):
    question: str
    test_type: str  
    category: str  
    correct_answer: str
    responseA: str
    responseB: str
    responseC: str
    responseD: Optional[str]
    remark: Optional[str]

# Admin-only Endpoint to create a new question
@router.post("/create_question")
def create_question(
    question_data: QuestionCreate,  # The new question data provided by the admin
    admin_user: dict = Depends(get_admin_user)  # Ensure only admins can access this
):
    """
    Admin-only endpoint to create a new question.
    Only users with the admin role can access this endpoint.
    """
    
    # You can add logic here to save the question in the database or Excel file
    new_question = {
        "question": question_data.question,
        "test_type": question_data.test_type,
        "category": question_data.category,
        "correct_answer": question_data.correct_answer,
        "responseA": question_data.responseA,
        "responseB": question_data.responseB,
        "responseC": question_data.responseC,
        "responseD": question_data.responseD,
        "remark": question_data.remark
    }
    # Append the question to the Excel file
    append_question_to_excel(new_question)
    
    # Return success message
    return {
        "status": "success",
        "message": "Question created successfully",
        "created_by": admin_user,
        "question": new_question
    }
