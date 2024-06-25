from settings import app
from utils.models import TextToProcess
from utils.diff_func import tokenize_text, pos_tag_text, ner_text


@app.post("/tokenize")
async def tokenize(text_to_process: TextToProcess):
    """ Endpoint that tokenizes text from a POST request """
    result = await tokenize_text(text_to_process.text)
    return {"text": result}


@app.post("/pos_tag")
async def pos_tag(text_to_process: TextToProcess):
    """ Endpoint that performs pos on text from a POST request """
    result = await pos_tag_text(text_to_process.text)
    return {"text": result}


@app.post("/ner")
async def ner(text_to_process: TextToProcess):
    """ Endpoint that performs ner on text from a POST request """
    result = await ner_text(text_to_process.text)
    return {"text": result}
