from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

ollama_chat_model = OpenAIModel(
    model_name="mistral:7b",
    provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)
