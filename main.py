from fastapi import FastAPI
from mangum import Mangum
from app.api.v1.endpoints import users, create_question
from app.api.v1.endpoints import generate_questions

app = FastAPI()
handler = Mangum(app)

# Register routers
app.include_router(users.router, prefix="/api/v1", tags=["Users"])
app.include_router(generate_questions.router, prefix="/api/v1", tags=["Questions"])
app.include_router(create_question.router, prefix="/api/v1", tags=["Admin"])



@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Application"}



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


