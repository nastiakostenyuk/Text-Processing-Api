from fastapi import FastAPI
import nltk

app = FastAPI()

nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
