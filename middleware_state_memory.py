from langchain.agents import AgentState,create_agent
from langchain.agents.middleware import AgentMiddleware
from typing import Any

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI( model="gemini-2.5-flash")

class CustomState(AgentState):
    user_preference : dict

class CustomMiddleware(AgentMiddleware):
    state_schema = CustomState
    tools = [tool1 , tool2 ]

    def before_model(self,CustomState, runtime)->dict[str,Any]| None:
        ...

agent = create_agent(model=model)

# The agent can now track additional state beyond messages
result = agent.invoke({
    "messages": [{"role": "user", "content": "I prefer technical explanations"}],
    "user_preferences": {"style": "technical", "verbosity": "detailed"},
})