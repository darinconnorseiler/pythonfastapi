from fastapi import FastAPI

app = FastAPI()
#Testing commit
@app.get("/login")
def root():
    return {"message": "Welcome to my api"}
