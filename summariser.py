# summariser.py
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


def summarise_comments(comments: list[str]) -> dict:
    """
    Summarise a list of ticket comments into 
    structured format
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.2
    )
    
    # Join all comments
    comments_text = "\n".join([
        f"Comment {i+1}: {c}" 
        for i, c in enumerate(comments)
    ])
    
    prompt = PromptTemplate(
        input_variables=["comments"],
        template="""
        You are a technical support engineer. 
        Summarise these ticket comments clearly.
        
        Comments:
        {comments}
        
        Provide a structured summary with:
        1. PROBLEM: What is the issue?
        2. STEPS TRIED: What solutions were attempted?
        3. CURRENT STATUS: Is it resolved or ongoing?
        4. NEXT ACTION: What should be done next?
        
        Be concise. Maximum 5 lines total.
        """
    )
    
    chain = prompt | llm
    result = chain.invoke({"comments": comments_text})
    
    return {
        "total_comments": len(comments),
        "summary": result.content
    }
