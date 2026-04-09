from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelResponse, ModelRequest
from langchain.tools import BaseTool, tool
from typing import Callable
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")


@tool
def public_search(query: str) -> str:
    """Public search endpoint for basic testing."""
    return f"[PUBLIC] test result for: {query}"


@tool
def private_serch(query: str) -> str:
    """Private search endpoint for auth-gated testing."""
    return f"[PRIVATE] test result for: {query}"


@tool
def advanced_search(query: str) -> str:
    """Advanced search endpoint for later-stage conversation testing."""
    return f"[ADVANCED] test result for: {query}"


def filter_tools_by_state(
    tools: list[BaseTool],
    is_authenticated: bool,
    message_count: int,
) -> list[BaseTool]:
    """Return only the tools allowed for the current conversation state."""
    if not is_authenticated:
        return [t for t in tools if t.name.startswith("public_")]
    if message_count < 5:
        return [t for t in tools if t.name != "advanced_search"]
    return tools

@wrap_model_call
def state_based_tools (
    request : ModelRequest,
    handler : Callable[[ModelRequest],ModelResponse]
) -> ModelResponse:
    
    """Filter tools based on conversation State."""
     # Read from State: check if user has authenticated
    state = request.state
    is_authenticated = state.get("authenticated",False)
    message_count = len(state.get("messages", []))

    allowed_tools = filter_tools_by_state(
        request.tools,
        is_authenticated=is_authenticated,
        message_count=message_count,
    )
    request = request.override(tools=allowed_tools)

    return handler(request)
    
agent = create_agent(
    model=model,
    tools=[public_search, private_serch, advanced_search],
     middleware=[state_based_tools]
)


def run_filter_demo() -> None:
    """Print expected tool access for key test states."""
    all_tools = [public_search, private_serch, advanced_search]
    scenarios = [
        ("Case 1: unauthenticated", False, 1),
        ("Case 2: authenticated, early chat", True, 2),
        ("Case 3: authenticated, 5+ messages", True, 6),
    ]

    for label, authenticated, message_count in scenarios:
        allowed = filter_tools_by_state(
            all_tools,
            is_authenticated=authenticated,
            message_count=message_count,
        )
        allowed_names = ", ".join(tool.name for tool in allowed)
        print(f"{label} -> {allowed_names}")


if __name__ == "__main__":
    run_filter_demo()