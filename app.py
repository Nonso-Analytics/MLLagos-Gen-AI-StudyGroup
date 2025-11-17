import os
import time
import google.generativeai as genai
from google.api_core import exceptions
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class GeminiCLI:
    """Backend interface for Google's Gemini API"""
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-2.5-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Set GEMINI_API_KEY in .env or pass directly.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)
        self.max_retries = 3
        self.base_delay = 1  # seconds

    def _validate_input(self, question: str) -> bool:
        """Validate user input before sending to API"""
        if not question or len(question.strip()) == 0:
            raise ValueError("Question cannot be empty")
        if len(question) > 10000:
            raise ValueError("Question too long (max 10000 characters)")
        return True
    
    def ask(self, question: str) -> str:
        """Send a question to Gemini and return response"""
        self._validate_input(question) 
        for attempt in range(self.max_retries):
            try:
                response = self.model.generate_content(question)
                if not response.text:
                    return "No response generated."
                return response.text
            except exceptions.ResourceExhausted:
                time.sleep(self.base_delay * (2 ** attempt))
            except exceptions.GoogleAPIError as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.base_delay * (2 ** attempt))
                else:
                    return f"API Error: {e}"
        return "Failed after retries."
    
    
    

