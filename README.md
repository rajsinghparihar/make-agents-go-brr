# make-agents-go-brr
I try out crewai for multiple usecases. This project is an attempt to learn agentic flow and execution of complex tasks in a simplified manner.

### Dec 30th 2024
- Explored the NL2SQL tool provided as part of crewai's toolkit
- created a simple data analysis agent using crewai in coding_agent.py
- explored crewai flows


### Jan 3rd 2025
One of the hardest parts of this problem is creating a natural language to SQL agent that can handle complex databases.
Solving this might solve majority of the problems that rely on this.

This time I created a market research crew using crewai's flows

defined in market_research/research_crew.py the class ResearchFlow defines the flow for the agent's execution
it follows the following tasks

- the `input_function` is the entrypoint for the agent which takes a topic (say Top 10 best EVs in 2024)
- the research agent then kicks off the `analysis_crew` on the output of the `input_function` [which is the topic: Top 10 best EVs in 2024] which contains the `research_task` and `news_agent` (news_agent is just an LLM with access to the `websearch_tool` using the serper.dev API)
- then the `filter_data` function is executed which takes the output of this function
  - a python parsable list of the names of things defined in the topic (top 10 EVs in 2024)

- In the `filter_data` function I've simulated the database fetch by associating some random revenue to each of those elements from the output of the previous function.
- I plan to replace this step by using the NL2SQL tool on a MySQL database with some transactions dataset on my local machine.

- the final function `get_insights` is taking this structured data and feeding it to an LLM to generate a report.


Now the post processing steps are remaining like creating a pdf from markdown using some library but will do that after implementing the NL2SQL logic for the data fetch from db.