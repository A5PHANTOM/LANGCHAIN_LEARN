from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool,ToolRuntime
from langgraph.checkpoint.memory import InMemorySaver
from dataclasses import dataclass
model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash"
)

agent = create_agent(
    model=model,
    system_prompt= """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""
)

@tool
def get_weather_for_location(city:str)->str:
    """Get weather for a given city"""
    return f"It's always sunny in {city}!"

@dataclass
class Context:
    """Custom runtime context schema"""
    user_id :str

@tool 
def get_user_location(runtime: ToolRuntime[Context])->str:
    """ Retrieve user information based on User ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id=="1" else "SF"

@dataclass
class ResponseFormat:
    """Response schema for Agent"""
    #A punny response is always needed
    punny_response : str
    # Any interesting information about the weather if available
    weather_condition : str | None = None



