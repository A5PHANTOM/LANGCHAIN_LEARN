from langchain_groq import ChatGroq
from langchain.messages import SystemMessage,HumanMessage, AIMessage
model = ChatGroq(model="llama-3.1-8b-instant")


sys_msg = SystemMessage("You are a helpfull agent")
hum_msg = HumanMessage("tell me a joke")
ai_msg = AIMessage("Why did the programmer quit his job? Because he didn't get arrays.")


message = [sys_msg,hum_msg]

response = model.invoke(message)

print(response.content)




