from langchain_core.prompts import ChatPromptTemplate

class OpenAIToolsAgent:
    prompt = """
================================ System Message ================================

You are a helpful assistant

============================= Messages Placeholder =============================

{chat_history}

================================ Human Message =================================

{input}

============================= Messages Placeholder =============================

{agent_scratchpad}
"""
    template_prompt = ChatPromptTemplate.from_template(prompt)
    
# print("asdadsdsa")
# print("wkwkwk")