**LANGCHAIN** : is an open-source framework designed to simplify building applications powered by Large Language Models (LLMs) like GPT-4 and Claude . It acts as an orchestration layer, enabling developers to connect LLMs to external data sources, APIs, and computation for creating complex, context-aware AI tools. 

**TOOLS** : Tools give agents the ability to take actions. Agents go beyond simple model-only tool binding by facilitating:
-Multiple tool calls in sequence (triggered by a single prompt)
-Parallel tool calls when appropriate
-Dynamic tool selection based on previous results
-Tool retry logic and error handling
-State persistence across tool calls


# @tool decorator is the most common and easiest way to turn a simple Python function into a LangChain Tool.

# When you use @tool, LangChain automatically converts your function's metadata (its name, its type hints, and its docstring) into a JSON Schema that an LLM (like GPT-4) can understand and decide when to call.

***Static tools*** : Static tools are defined when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.

***Dynamic tools*** : the set of tools available to the agent is modified at runtime rather than defined all upfront. Not every tool is appropriate for every situation. Too many tools may overwhelm the model (overload context) and increase errors; too few limit capabilities. Dynamic tool selection enables adapting the available toolset based on authentication state, user permissions, feature flags, or conversation stage.

There are two approaches depending on whether tools are known ahead of time:

1.*Filtering pre-registered tools* :When all possible tools are known at agent creation time, you can pre-register them and dynamically filter which ones are exposed to the model based on state, permissions, or context.
        -3 methords :  
        *State* : Enable advanced tools only after certain conversation milestones
        *Store*
        *Runtime Context*
2.*Runtime tool registration* : When tools are discovered or created at runtime (e.g., loaded from an MCP server, generated based on user data, or fetched from a remote registry), you need to both register the tools and handle their execution dynamically.

This requires two middleware hooks:
**wrap_model_call** - Add the dynamic tools to the request
**wrap_tool_call** - Handle execution of the dynamically added tools

**ReAct Loop** : Agents follow the ReAct (“Reasoning + Acting”) pattern, alternating between brief reasoning steps with targeted tool calls and feeding the resulting observations into subsequent decisions until they can deliver a final answer.


**SYSTEM PROMPTING** :You can shape how your agent approaches tasks by providing a prompt. 
<!-- agent = create_agent(
    model,
    tools,
    system_prompt="You are a helpful assistant. Be concise and accurate."
) -->

**Dynamic system prompt** :For more advanced use cases where you need to modify the system prompt based on runtime context or agent state, you can use middleware.

- The @dynamic_prompt decorator creates middleware that generates system prompts based on the model request

**NAME** : Set an optional name for the agent. This is used as the node identifier when adding the agent as a subgraph in multi-agent systems
<!-- agent = create_agent(
    model,
    tools,
    name="research_assistant"
) -->

**Invocation** :You can invoke an agent by passing an update to its State. All agents include a sequence of messages in their state; to invoke the agent, pass a new message

<!-- result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
) -->

# ADVANCED CONCEPTS

***Structured Output*** :In some situations, you may want the agent to return an output in a specific format. LangChain provides strategies for structured output via the response_format parameter.

- **ToolStrategy** : ToolStrategy uses artificial tool calling to generate structured output. This works with any model that supports tool calling

# MEMORY

Agents maintain conversation history automatically through the message state. You can also configure the agent to use a custom state schema to remember additional information during the conversation

Information stored in the state can be thought of as the short-term memory of the agent:
Custom state schemas must extend AgentState as a TypedDict.
There are two ways to define custom state:
Via middleware (preferred)
Via state_schema on create_agent

***​Defining state via middleware*** : Use middleware to define custom state when your custom state needs to be accessed by specific middleware hooks and tools attached to said middleware.


# Streaming
f the agent executes multiple steps, this may take a while. To show intermediate progress, we can stream back messages as they occur.


 **temperature** : Controls the randomness of the model’s output. A higher number makes responses more creative; lower ones make them more deterministic.


**max_tokens** : Limits the total number of tokens in the response, effectively controlling how long the output can be.

**timeout number** : The maximum time (in seconds) to wait for a response from the model before canceling the request.

# MESSAGING

System message — defines the assistant's behavior/role
User message — first request
Assistant message — first response (already provided as context)
User message — second request (the one the model needs to respond to)

# Batch
Batching a collection of independent requests to a model can significantly improve performance and reduce costs, as the processing can be done in parallel


# Structured output

Models can be requested to provide their response in a format matching a given schema. This is useful for ensuring the output can be easily parsed and used in subsequent processing. LangChain supports multiple schema types and methods for enforcing structured output.


 # Reasoning

Many models are capable of performing multi-step reasoning to arrive at a conclusion. This involves breaking down complex problems into smaller, more manageable steps.


# MESSAGES
Messages are the fundamental unit of context for models in LangChain. They represent the input and output of models, carrying both the content and metadata needed to represent the state of a conversation when interacting with an LLM.
Messages are objects that contain:
 Role - Identifies the message type (e.g. system, user)
 Content - Represents the actual content of the message (like text, images, audio, documents, etc.)
 Metadata - Optional fields such as response information, message IDs, and token usage

**Message types**
 System message - Tells the model how to behave and provide context for interactions
 Human message - Represents user input and interactions with the model
 AI message - Responses generated by the model, including text content, tool calls, and metadata
 Tool message - Represents the outputs of tool calls