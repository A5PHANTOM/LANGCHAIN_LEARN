from langchain_groq import ChatGroq
from langchain.agents import create_agent

model = ChatGroq(
    model="llama-3.1-8b-instant",
    timeout = 30,
)

conversation = [
    {"role": "system", "content": "You are a helpful assistant that translates English to French."},
    {"role": "user", "content": "Translate: I love programming."},
    {"role": "assistant", "content": "J'adore la programmation."},
    {"role": "user", "content": "Translate: I love building applications."}
]

response = model.invoke(conversation)
print(response.content)  # AIMessage("J'adore créer des applications.")