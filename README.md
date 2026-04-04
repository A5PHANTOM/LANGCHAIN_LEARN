**LANGCHAIN** : is an open-source framework designed to simplify building applications powered by Large Language Models (LLMs) like GPT-4 and Claude . It acts as an orchestration layer, enabling developers to connect LLMs to external data sources, APIs, and computation for creating complex, context-aware AI tools. 

**TOOLS** : Tools give agents the ability to take actions. Agents go beyond simple model-only tool binding by facilitating:
-Multiple tool calls in sequence (triggered by a single prompt)
-Parallel tool calls when appropriate
-Dynamic tool selection based on previous results
-Tool retry logic and error handling
-State persistence across tool calls

***Static tools*** : Static tools are defined when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.
