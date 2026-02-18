from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
#from tavily import TavilyClient
from langchain_tavily import TavilySearch

#tavily = TavilyClient()

load_dotenv()


def main():
    print("Hello from langgraph-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for Tokyo weather")})
    print(result)

#@tool    
#def search(query:str) -> str:
#    """
#    Tool that searches over the internet
    
#    Args:
#        query : The query to search for
#    Returns:
#        The search result
#    """
#    print(f"Searching for {query}")
#    return tavily.search(query=query)

llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)

if __name__ == "__main__":
    main()
