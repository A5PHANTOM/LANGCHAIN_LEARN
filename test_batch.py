from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage,SystemMessage
model = ChatGroq(
    model="llama-3.1-8b-instant",
    timeout = 30,
)
responses = model.batch([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
])

for response in responses:
   print(response.content)
