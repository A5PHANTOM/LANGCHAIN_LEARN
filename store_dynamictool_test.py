from dataclasses import dataclass
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.middleware import ModelRequest,ModelResponse,wrap_model_call
from typing import Callable
from langgraph.store.memory import InMemoryStore


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")

@dataclass
class Context :
    user_id : str

@wrap_model_call
def store_based_tools(
    request : ModelRequest,
    handle : Callable[[ModelRequest],ModelResponse]
) -> ModelResponse :
     """Filter tools based on Store preferences."""
     user_id = request.runtime.context.user_id

    # Read from Store: get user's enabled features
     store = request.runtime.store
     feature_flag = store.get(("features",),user_id)


     if feature_flag :
          enabled_features = feature_flag.value.get("enabled_tools",[])
           # Only include tools that are enabled for this user
          tools = [t for t in request.tools if t.name in enabled_features]
          request = request.override(tools=tools)

          return handle(request)

agent = create_agent(
     model=model,
     tools=[search_tool, analysis_tool, export_tool],
    middleware=[store_based_tools],
    context_schema=Context,
    store=InMemoryStore()
)
