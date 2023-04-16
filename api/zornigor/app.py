
from fastapi import FastAPI


app = FastAPI(title="Zornigor API")


@app.get("/")
async def root():
    return {
        "message": "Welcome to Zornigor API"
    }
