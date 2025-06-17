from pydantic_ai.agent import Agent
from model_init import ollama_chat_model
from pydantic_classes import PaperAbstract
import pypdf

pdf_path = "C:/Personal/Personal Projects/research_paper_abstractor/paper_1.pdf"
path = "C:/Personal/Personal Projects/research_paper_abstractor/prompts/abstract_extractor.txt"
with open(path, "r", encoding="utf-8") as f:
    prompt_txt = f.read()

reader = pypdf.PdfReader(pdf_path)
page = reader.pages[0]
text = page.extract_text()
print(text)

abstract_agent = Agent (
    model=ollama_chat_model,
    result_type=PaperAbstract,
    system_prompt= (
        prompt_txt
    ),
)
print(abstract_agent)

response = abstract_agent.run_sync(user_prompt=text)
print(response)