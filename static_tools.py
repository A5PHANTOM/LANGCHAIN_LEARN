from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")

@tool
def search(query:str) -> str:
    """search for information"""
    return f"Result for : {query}"

@tool
def get_weather(location:str)->str:
    """Get Weather information for a location."""
    return f"Weather in {location} is sunny, 72°F"

agent = create_agent(
    model=model,
    tools=[search,get_weather])

response = agent.invoke(
        {"messages": [{"role": "user", "content": "What is the weather in Kochi?"}]}
    )
print(response["messages"][-1].content)

