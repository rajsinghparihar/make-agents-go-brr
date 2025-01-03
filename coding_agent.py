from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

load_dotenv(".env", override=True)
llm = LLM(model="groq/gemma2-9b-it", temperature=0.3)
# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True,
    llm=llm,
)

# Create a task that requires code execution
data_analysis_task = Task(
    name="coding task",
    description="Analyze the given dataset by reading 'workspace/particles.csv' and calculate the average age of participants. also you need to calculate the rank of each of the participants based on their age and output their names in the order of their rank",
    agent=coding_agent,
    expected_output="The output of the python code in string format",
)

# Create a crew and add the task
analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[data_analysis_task],
    verbose=True,
    planning=True,
    planning_llm=llm,
)

# Execute the crew
result = analysis_crew.kickoff()

print(result)
