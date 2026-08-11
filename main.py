import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import langchainhub as hub
import pandas as pd
from groq import Groq

# Load environment Variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Setup Tavily Search
search = TavilySearchResults(max_results = 5)
result = search.invoke("Chennai Weather")

# LLM Setup
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

# Setup Tool
tools = [search]

# Setup Agent

SYSTEM_PROMPT = """You are an Autonomous ReAct AI Research Assistant. You operate strictly using a continuous loop of Reasoning, Action, Observation, and Synthesis.

### EXECUTION STEPS:
1. **THINK**: Analyze the user input. Identify missing information, key entities, and required tool calls.
2. **ACT**: Execute search tools with optimized keywords. Search one atomic concept at a time.
3. **OBSERVE**: Analyze search tool outputs. Check if the retrieved data directly answers the query.
4. **SYNTHESIZE**: Synthesize the observations into an structured, well-organized response.

### CRITICAL CONSTRAINTS:
- Do NOT answer questions requiring external facts without calling the search tool first.
- Maintain an objective, professional, and analytical tone.
- Format complex comparative data using Markdown tables or itemized bullet points.
"""
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)
print("\n" + "="*50 + "\n")
userinput = input("Enter Your Query: ")

# Setup executer
response = agent.invoke({
    "messages": [
        {"role": "user", "content": userinput}
    ]
})
print("\n" + "="*50 + "\n")
print(response["messages"][-1].content)
