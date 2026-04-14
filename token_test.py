from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage,SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.callbacks import UsageMetadataCallbackHandler


model = ChatGroq(
    model="llama-3.1-8b-instant",
    timeout = 30,
)

callback = UsageMetadataCallbackHandler()
result_1 = model.invoke("Hello", config={"callbacks": [callback]})
print(callback.usage_metadata)