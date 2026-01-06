from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

def pretty_print_messages(messages_dict):
    """Pretty print LangGraph message history"""
    messages = messages_dict.get('messages', [])
    
    for i, msg in enumerate(messages, 1):
        print(f"\n{'-'*80}")
        print(f"Message {i}: {msg.type.upper()}")
        
        if isinstance(msg, HumanMessage):
            print(f"User Message: {msg.content}")
            
        elif isinstance(msg, AIMessage):
            if msg.content:
                print(f"AI Message: {msg.content}")
            
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                print(f"Tool calls made by AI:")
                for tool_call in msg.tool_calls:
                    print(f"Tool Name: {tool_call['name']}")
                    print(f"Arguments Passed: {tool_call['args']}")
                    
        elif isinstance(msg, ToolMessage):
            print(f"Tool output from: {msg.name}")
            print(f"Result (first 200 characters): {msg.content[:200]}...")

