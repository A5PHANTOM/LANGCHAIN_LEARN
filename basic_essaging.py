from langchain_groq import ChatGroq
from langchain.messages import SystemMessage,HumanMessage
model = ChatGroq(model="llama-3.1-8b-instant")


sys_msg = SystemMessage("You are a helpfull agent")
hum_msg = HumanMessage("tell me a joke")

message = [sys_msg,hum_msg]

response = model.invoke(message)

print(response.content)




