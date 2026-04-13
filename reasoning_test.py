
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage,SystemMessage
model = ChatGroq(
    model="llama-3.1-8b-instant",
    timeout = 30,
)

for chunk in model.stream("Why do parrots have colorful feathers?"):
    reasoning_steps = [r for r in chunk.content_blocks if r["type"] == "reasoning"]
    print(reasoning_steps if reasoning_steps else chunk.text)