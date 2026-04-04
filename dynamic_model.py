from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest,ModelResponse,wrap_model_call
from langchain.tools import tool

basic_model = ChatGoogleGenerativeAI( model = "gemini-2.5-flash")
advanced_model = ChatGroq(model="llama-3.1-8b-instant")

@wrap_model_call
def dynamic_model_selection(request : ModelRequest, handler) -> ModelResponse:
     """Choose model based on conversation complexity."""
     message_count = len(request.state["messages"])
     if message_count >10 :
          print("advanced model activated")
          model = advanced_model
     else :
          print("basic model activated")
          model = basic_model

     return handler(request.override(model=model))

agent = create_agent(
     model=basic_model,
     middleware=[dynamic_model_selection]
)

result = agent.invoke(
    {
       "messages": [{"role":"user","content":"tell me about what is ai and what are the advantages of ai (give 5 examples)"}]
    }
 )

print(result)