import uvicorn


from settings import app
from utils.endpoints import tokenize, pos_tag, ner


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
