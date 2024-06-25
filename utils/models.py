from pydantic import BaseModel


class TextToProcess(BaseModel):
    text: str
