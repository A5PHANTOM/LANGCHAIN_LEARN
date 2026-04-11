from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage,HumanMessage

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")

agent = create_agent(
    model= model,
    system_prompt=SystemMessage(
        content=[
            {
            "type":"text",
            "text":"You are an AI assistant tasked with analyzing literary works.",
            },
            {
                "type": "text",
                "text": "<the entire contents of 'Pride and Prejudice'>",
                "cache_control": {"type": "ephemeral"}
            }
        ]
    )
)


result = agent.invoke(
    {"messages":[HumanMessage("Analyze the major themes in 'Pride and Prejudice'.")]}
)

print(result)