**LANGCHAIN** : is an open-source framework designed to simplify building applications powered by Large Language Models (LLMs) like GPT-4 and Claude . It acts as an orchestration layer, enabling developers to connect LLMs to external data sources, APIs, and computation for creating complex, context-aware AI tools. 

**TOOLS** : Tools give agents the ability to take actions. Agents go beyond simple model-only tool binding by facilitating:
-Multiple tool calls in sequence (triggered by a single prompt)
-Parallel tool calls when appropriate
-Dynamic tool selection based on previous results
-Tool retry logic and error handling
-State persistence across tool calls

***Static tools*** : Static tools are defined when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.

***Dynamic tools*** : the set of tools available to the agent is modified at runtime rather than defined all upfront. Not every tool is appropriate for every situation. Too many tools may overwhelm the model (overload context) and increase errors; too few limit capabilities. Dynamic tool selection enables adapting the available toolset based on authentication state, user permissions, feature flags, or conversation stage.

There are two approaches depending on whether tools are known ahead of time:

1.*Filtering pre-registered tools* :When all possible tools are known at agent creation time, you can pre-register them and dynamically filter which ones are exposed to the model based on state, permissions, or context.
        -3 methords :  
        *State* : Enable advanced tools only after certain conversation milestones
        *Store*
        *Runtime Context*


