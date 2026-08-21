import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_agent
import langchainhub as hub
from langchain_groq import ChatGroq
import pandas as pd
from groq import Groq
from langchain_core.tools import tool
import requests, json
import streamlit as st

# Load environment Variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
weather_stack_api = os.getenv("WEATHER_STACK_API")

# Setup Tavily Search
search = TavilySearchResults(max_results = 2)

@tool
def fetch_weather(city : str) -> str:
    """Fetch the Current weather for the city"""
    url = (f"http://api.weatherstack.com/current?access_key={weather_stack_api}&query={city}")
    response = requests.get(url)
    data = response.json()
    current = data.get("current", {})
    location = data.get("location", {})
    weather_data = {
        "Name": location.get("name"),
        "Temperature": current.get("temperature"),
        "Description": current.get("weather_descriptions"),
        "Humidity" : current.get("humidity")
    }
    return json.dumps(weather_data)

# LLM Setup
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens=500
)

# Setup Tool
tools = [fetch_weather, search]

# Setup Agent with Appropriate Prompt
SYSTEM_PROMPT = """
- Your Name is Echo
When answering questions using tools results:
- Use all relevant information returned by the tools.
- Do not ignore useful fields.
- For detailed answers, explain each relevant field.
- For brief answers, summarize only the most important fields.
- Summarize and stick with 6000 Tokens
"""
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)


# Setup executer - Debug

# print("\n" + "="*50 + "\n")
# userinput = input("Enter Your Query: ")
# response = agent.invoke({
#     "messages": [
#         {"role": "user", "content": userinput}
#     ]
# })
# print("\n" + "="*50 + "\n")
# print(response["messages"][-1].content)


# Custom Tools creation using functions also works



