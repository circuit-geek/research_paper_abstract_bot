from pydantic import BaseModel
from pydantic_ai.agent import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

class BasicMessage(BaseModel):
    capital: str

ollama_model = OpenAIModel(
    model_name="qwen3:1.7b",
    provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)

agent = Agent(
    model=ollama_model,
    result_type= BasicMessage,
    system_prompt= (
        "Your geography expert who knows the capital of all the countries"
    ),
)

result = agent.run_sync("What is the capital of India?")
print(result.output)