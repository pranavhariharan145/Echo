import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
import pandas as pd

# Load environment Variables
load_dotenv()
deep_api_key = os.getenv("DEEPSEEK_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Setup Tavily Search

search = TavilySearchResults(max_results = 1)

result = search.invoke("Capital of France")
print(result)
