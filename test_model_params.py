from langchain_groq import ChatGroq
from langchain.agents import create_agent

model = ChatGroq(
    model="llama-3.1-8b-instant",
    timeout = 30,
)

response = model.invoke("Why do parrots have colorful feathers?")

print(response.content)