from crewai import Agent, Task, Crew, LLM
from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import random
import ast

load_dotenv(".env", override=True)
llm = LLM(model="groq/gemma2-9b-it", temperature=0.3)
brain_llm = LLM(model="groq/llama-3.3-70b-specdec", temperature=0.3)
# Create an agent with code execution enabled
websearch_tool = SerperDevTool()
decomposer_agent = Agent(
    role="Query Decomposer",
    goal="To Decompose the user's query into subtasks that are easy to manage",
    backstory="You are an experienced manager who understands user inputs and breaks them into smaller manageable tasks.",
    llm=llm,
)

news_agent = Agent(
    role="Senior Researcher",
    goal="Search information about {topic}",
    backstory=(
        "Driven by profits and novelity in the research business, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could help the business profit."
    ),
    llm=llm,
    tools=[websearch_tool],
    allow_delegation=True,
)

summary_agent = Agent(
    role="Summary Generator",
    goal="Generate summary from fetched data",
    backstory="A seasoned business analyst who has deep understanding of data and can generate meaningful insights from it",
    verbose=True,
    llm=brain_llm,
)

# Create a task that requires code execution
research_task = Task(
    description=("Identify the {topic}"),
    expected_output="A list of the name of {topic} without additional text or description.",
    tools=[websearch_tool],
    agent=news_agent,
    # human_input=True,
)

summary_task = Task(
    description="Generate summary of the fetched_data: {fetched_data}",
    expected_output="A complete report about all the information that can help the business profit and take optimal decisions.",
    agent=summary_agent,
)

# Create a crew and add the task
analysis_crew = Crew(
    agents=[news_agent],
    tasks=[research_task],
    verbose=True,
    planning=True,
    planning_llm=llm,
)

summary_crew = Crew(
    agents=[summary_agent],
    tasks=[summary_task],
    verbose=True,
    planning=True,
    planning_llm=brain_llm,
)


class ResearchFlow(Flow):
    @start()
    def input_function(self):
        user_query = input("Enter a topic: ")
        print(f"User query: {user_query}")
        return user_query

    @listen(input_function)
    def run_research(self, user_query):
        print(f"Researching the topic: {user_query}")
        result = analysis_crew.kickoff(inputs={"topic": user_query})
        print(result)

        return result

    @listen(run_research)
    def filter_data(self, research_result):
        print("Getting data from internal sources")
        print("Filtering results")
        filtered_results = []
        parsed_results = ast.literal_eval(research_result.raw)
        for res in list(parsed_results):
            filtered_results.append(
                {"name": res, "revenue": random.randint(int(1e7), int(1e8))}
            )
        print(filtered_results)

        return filtered_results

    @listen(filter_data)
    def get_insights(self, filtered_data):
        print("Generating Report")
        final_report = summary_crew.kickoff(inputs={"fetched_data": filtered_data})
        return final_report


research_flow = ResearchFlow()
research_flow.plot("research_flow")

result = research_flow.kickoff()
print(result)
