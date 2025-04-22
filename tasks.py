from crewai import Task
from tools import yt_tools
from agents import blog_reseracher,blog_writer


# Reseach task
research_task = Task(
    description = (
        "Indentify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 paragraph long report based on the {topic} of video content ',
    tools=[yt_tools],
    agent=blog_reseracher,
)


# Writing task with language model configuration
write_task = Task(
    description = (
        "get the info from the youtube channel on the topic {topic}."
    ),
    expected_output='Summarize the content form the Youtube Channel and write a detailed long structured Article from the Youtube Chanel Video based on the {topic}',
    tools=[yt_tools],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'

)