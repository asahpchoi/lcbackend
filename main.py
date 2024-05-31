from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/Testing")
def Testing():
    return {"Tesitn":"FDAS"}