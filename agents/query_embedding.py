from pydantic_classes import QueryEmbeddings
import ollama

def get_embeddings(query):
    embeddings = ollama.embeddings(model="nomic-embed-text:v1.5", prompt=query)
    json_embed = embeddings.model_dump()
    valid_response = QueryEmbeddings.model_validate(json_embed)
    return valid_response
