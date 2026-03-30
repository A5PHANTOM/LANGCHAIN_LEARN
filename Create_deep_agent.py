#deepagents is a standalone library built on top of LangChain’s core building blocks for agents. 
# It uses the LangGraph runtime for durable execution, streaming, human-in-the-loop, and other features.

from deepagents import create_deep_agent

def get_weather (city : str) ->str :
    """ Get Weather for given city """
    return f"Its always sunny at {city}"

agent = create_deep_agent(
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)

#Run the agent 
agent.invoke(
    {"message":[{"role":"user","content":"what is the weather in sf"}]}
)





