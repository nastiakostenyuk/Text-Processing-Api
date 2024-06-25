# Text Processing Api
This is a simple Text Processing Api for different text operations 


## SETUP
### 1. Create a virtual environment:
  - python -m venv env
  - source env/bin/activate  # On Windows use `env\Scripts\activate`

### 2.Install dependencies:
  - pip install -r requirements.txt

### 3.Run the application:
  - uvicorn app:app --reload

### 4.Test the endpoint:
  - Open http://127.0.0.1:8000/docs. 
  - Here we can send post requests different endpoints for testing. 

### Endpoints:

#### 1. /tokenize - Endpoint that tokenizes text:
    {method: POST, 
    parameters: json with a field 'text',
    response: json with a field 'text'}

#### 2. /pos_tag - Endpoint that performs pos on text:
    {method: POST, 
    parameters: json with a field 'text',
    response: json with a field 'text'}

#### 2. /ner - Endpoint that performs ner on text:
    {method: POST, 
    parameters: json with a field 'text',
    response: json with a field 'text'}
