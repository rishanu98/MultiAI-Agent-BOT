import os
from crewai import Agent, LLM
#from langchain.llms import Ollama
from tools import yt_tools
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

env_path = Path("D:\Anaconda\envs\crewai_env\.env")
load_dotenv(dotenv_path=env_path)

groq_api_key = os.getenv("GROQ_API_KEY")
#os.environ['OPENAI_API_KEY'] = os.getenv["OPENAI_API_KEY"]
#ollama_llm = LLM(model="llamma3", base_url="http://localhost:11434")
os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN")
## Create a senior blog content researcher
llm = ChatGroq(model="groq/llama-3.3-70b-versatile",groq_api_key=groq_api_key)

blog_reseracher =  Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get the relevant video content for the topic: {topic}",
    name='Senior Youtube Content Researcher',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding video in AI Data Science, Machine Learning and GEN AI and providing suggestion"
    ),
    llm=llm,
    tools=[yt_tools],
    allow_delegation=True
)

## creating a senior blog writer agent with YT tool

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from YT channel",
    name='Senior Blog Content Researcher',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topic, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accesible manner"
    ),
    llm=llm,
    tools=[yt_tools],
    allow_delegation=False
)