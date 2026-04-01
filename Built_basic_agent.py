from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash"
)

def get_weather(city :str) ->str:
    """Get wether for city """
    return f"Its always sunny in {city} !"

agent=create_agent(
    model = model ,
    tools =[get_weather],
    system_prompt = "You are a heloful assistant"
    ,
)

#Run the agent 
result = agent.invoke(
    {
       "messages": [{"role":"user","content":"what is the weather in sf"}]
    }
 )

print(result)
