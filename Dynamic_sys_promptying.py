from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt,ModelRequest

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")

class Context (TypedDict):
    user_role :str

@dynamic_prompt
def user_role_prompt(request : ModelRequest)-> str:
    """Generate system prompt based on user role."""
    user_role = request.runtime.context.get("user_role","user")
    base_prompt = "You are a helpful assistant"

    if user_role == "expert":
         return f"{base_prompt} Provide detailed technical responses."
    elif user_role == "beginner":
         return f"{base_prompt} Explain concepts simply and avoid jargon."
    return base_prompt

agent = create_agent(
     model=model,
     middleware=[user_role_prompt],
     context_schema=Context

)
result = agent.invoke(
      {"messages": [{"role": "user", "content": "Explain machine learning"}]},
    context={"user_role": "beginner"}
)

print(result)