from fastapi import FastAPI
from mangum import Mangum
from app.api.v1.endpoints import users, create_question
from app.api.v1.endpoints import generate_questions
from app.api.v1.endpoints import test

app = FastAPI()
handler = Mangum(app)

# Register routers
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(generate_questions.router, prefix="/api/v1", tags=["questions"])
app.include_router(create_question.router, prefix="/api/v1", tags=["admin"])
app.include_router(test.router, prefix="/api/v1", tags=["test-api"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Application"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


