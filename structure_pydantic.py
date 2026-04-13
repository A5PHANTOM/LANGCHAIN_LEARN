from pydantic import BaseModel,Field
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage,SystemMessage
model = ChatGroq(
    model="llama-3.1-8b-instant",
    timeout = 30,
)

class Movie(BaseModel):
    """A movie with details."""
    title : str = Field (description="the title of the movie")
    year : int = Field(description="the year the movie was launched")
    director : str = Field(description="the director of the movie")
    rating : float = Field(description="The movie's rating out of 10")

Model_with_structure = model.with_structured_output(Movie)
response = Model_with_structure.invoke("provide details about the movie inception")
print(response)