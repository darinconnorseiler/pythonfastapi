from fastapi import FastAPI

app = FastAPI()
#Testing pull request
@app.get("/login")
def root():
    return {"message": "Welcome to my api"}
