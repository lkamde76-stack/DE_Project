from fastapi import FastAPI

app = FastAPI()
@app.get("/hello")
def hello():
    return("Hello Pravin to the new section")
@app.get("/")
def hello():
    return("Hello Pravin")