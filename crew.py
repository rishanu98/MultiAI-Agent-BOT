from crewai import Crew, Process
from agents import blog_reseracher, blog_writer
from tasks import research_task, write_task

crew = Crew(
    agents = [blog_reseracher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,
    verbose = True,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew=True
)
#inputs_array = {'topic': 'AI VS ML VS DL VS Data Science'}, {'topic': 'MCP Agentic AI Crash Course With Python'}
##start the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL VS Data Science'})
print(result)