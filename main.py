import uvicorn

from fastapi import FastAPI
from routers import hello_router

app = FastAPI()

app.include_router(
    hello_router
)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
