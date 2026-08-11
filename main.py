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
from langchain_core.tools import tool
import requests, json

# Load environment Variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
weather_stack_api = os.getenv("WEATHER_STACK_API")

# Setup Tavily Search
search = TavilySearchResults(max_results = 5)

@tool
def fetch_weather(city : str) -> str:
    """Fetch Current Weather of the city"""
    url = (f"http://api.weatherstack.com/current?access_key={weather_stack_api}&query={city}")
    response = requests.get(url)
    data = response.json()
    current = data.get("current", {})
    location = data.get("location", {})
    weather_data = {
        "Name": location.get("name"),
        "Country": location.get("country"),
        "Temperature": current.get("temperature"),
        "Description": current.get("weather_descriptions"),
        "Wind_Speed": current.get("wind_speed"),
        "Precipitation": current.get("precip"),
        "Humidity" : current.get("humidity"),
        "feelslike": current.get("feelslike"),
        "uv_index": current.get("uv_index")
    }
    return json.dumps(weather_data)

# LLM Setup
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1,
)

# Setup Tool
tools = [fetch_weather, search]

# Setup Agent with Appropriate Prompt
SYSTEM_PROMPT = """
When answering questions using tools results:
- Use all relevant information returned by the tools.
- Do not ignore useful fields.
- For detailed answers, explain each relevant field.
- For brief answers, summarize only the most important fields.
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


# Custom Tools creation using functions also works



