from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion


class ExampleFlow(Flow):
    model = "groq/gemma2-9b-it"

    @start()
    def generate_city(self):
        print("Starting flow")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world.",
                },
            ],
        )

        random_b = response["choices"][0]["message"]["content"]
        print(f"Random City: {random_b}")

        return random_b

    @listen(generate_city)
    def generate_fun_fact(self, random_b):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me which industry does {random_b} mainly deal in",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        return fun_fact


load_dotenv(".env", override=True)
flow = ExampleFlow()
result = flow.kickoff()

flow.plot("example_flow")

print(f"Generated fun fact: {result}")
