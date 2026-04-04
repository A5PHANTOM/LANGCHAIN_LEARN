from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key="",
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.1-8b-instant"
)

print(llm.invoke("Explain AI").content)