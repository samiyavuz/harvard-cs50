# It requires substantial environment configuration and was only done for illustrative purposes. 
# You should not attempt to run this code yourself, it would not work without openai API access!

from openai import OpenAI

client = OpenAI()

user_prompt = input("Prompt: ")
system_prompt = "Limit your answer to one sentence. Pretend you're a cat."

response = client.responses.create(
    input=user_prompt,
    instructions=system_prompt,
    model="gpt-5",
)

print(response.output_text)