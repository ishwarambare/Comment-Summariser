from fastapi import FastAPI
from pydantic import BaseModel
from summariser import summarise_comments as generate_summary

app = FastAPI(
    title="Comment Summariser API",
    description="An AI-powered API to summarise technical support ticket comments."
)

class SummariseRequest(BaseModel):
    comments: list[str]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Comment Summariser API"}

@app.post("/summarise")
def summarise_comments_endpoint(request: SummariseRequest) -> dict:
    """
    Summarise a list of comments using Google Gemini.
    """
    return generate_summary(request.comments)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)