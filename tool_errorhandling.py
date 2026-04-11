from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
     model ="gemini-2.5-flash"
)

@wrap_tool_call
def handle_tool_errors(request, handler):
     """Handle tool execution errors with custom messages."""
     try:
          return handler(request)
     except Exception as e:
          # Return a custom error message to the model
          return ToolMessage(
               content=f"Tool error: Please check your input and try again. ({str(e)})",
               tool_call_id=request.tool_call["id"],
          )
     
agent = create_agent(
     model=model,
     middleware=[handle_tool_errors]
)


