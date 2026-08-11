import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
import pandas as pd
from groq import Groq

# Load environment Variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Setup Tavily Search
search = TavilySearchResults(max_results = 5)
result = search.invoke("Chennai Weather")
df = pd.DataFrame(result)
print(df)

# LLM Setup
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)
result = llm.invoke("Joke about AI?")
print(result.content)