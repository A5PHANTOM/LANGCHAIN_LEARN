from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage,SystemMessage
model = ChatGroq(
    model="llama-3.1-8b-instant",
    timeout = 30,
)


for chunk in model.stream("What color is the sky?"):
    for block in chunk.content_blocks:
            print(block)
        