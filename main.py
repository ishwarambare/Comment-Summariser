from fastapi import FastAPI
from pydantic import BaseModel
from summariser import summarise_comments as generate_summary

app = FastAPI(
    title="Comment Summariser API",
    description="An AI-powered API to summarise technical support ticket comments."
)

'''
comments = [
    "Customer reports that the application crashes on startup.",
    "Support team suggested clearing cache and reinstalling, but issue persists.",
    "Customer provided logs showing a NullPointerException in the main module.",
    "Support team is investigating the logs and has escalated to the development team.",
    "Customer is awaiting further updates from support.",
    "Development team identified a potential memory leak in the latest release, which may be causing the crash.",
    "Customer is informed about the potential cause and is waiting for a patch from the development team."
]
'''


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
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)