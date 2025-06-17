from typing import List, Optional
from pydantic import BaseModel

class QueryEmbeddings(BaseModel):
    embedding: List[float]

class PaperAbstract(BaseModel):
    paper_num: Optional[int]
    title : Optional[str]
    authors: Optional[List[str]]
    keywords: Optional[List[str]]
    abstract: Optional[str]



