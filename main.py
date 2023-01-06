from fastapi import FastAPI

app = FastAPI()

@app.get("/login")
def root():
    return {"message": "Welcome to my api"}
