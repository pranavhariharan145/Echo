
# 🤖 Echo - LangChain AI Agent

A simple AI agent built with **LangChain, Tavily, Weatherstack, Groq, and Streamlit** that can use external tools to retrieve information and generate responses.

## 🌐 Live Demo

**[Try the AI Agent →](https://echo-kbuw.onrender.com)**

## 🚀 Features

* 🤖 LLM-powered AI agent for reasoning using Groq
* 🔧 Custom tool integration with LangChain
* 🌤️ Weather API (Weatherstack) integration
* 🔎 Tavily web search
* 🧠 LLM tool calling and agent orchestration
* 💬 Interactive Streamlit UI
* 📦 Dependency management using `uv`
* ☁️ Deployed on Render

## 🏗️ How It Works

```text
User
  ↓
Streamlit UI
  ↓
LangChain Agent
  ↓
Groq LLM
  ↓
Decides whether a tool is required
  ↓
┌──────────────────┐
│                  │
▼                  ▼
Weather Tool    Tavily Search
│                  │
▼                  ▼
Weather API     Search API
│                  │
└────────┬─────────┘
         ↓
    Tool Result
         ↓
        LLM
         ↓
   Final Response
         ↓
   Streamlit UI
```

The LLM determines which tool is required based on the user's request. LangChain then executes the selected tool and passes the result back to the LLM, which uses the information to generate the final response.

## 🛠️ Tech Stack

* Python
* LangChain
* Groq
* Streamlit
* Tavily
* `uv`
* Render

## 🧠 Key Concepts

This project was built to understand:
* Using Groq as LLM in terminal
* Using Tavily to search and provide results.
* Custom tool Creation, working with JSON response.
* LLM tool calling
* LangChain agents
* Tool schemas
* `AIMessage` and `ToolMessage`
* Agent orchestration
* External API integration
* Structured data passed between tools and LLMs
* Building and deploying LLM applications in web.

## 📁 Project Structure

```text
.
├── app.py
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

For starters: API keys must be kept outside the repository and should never be committed to GitHub.

## 👨‍💻 Author

**Pranav Hariharan**

A hands-on project exploring **LLM agents, tool calling, LangChain, and AI application development**.
