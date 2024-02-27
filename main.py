from fastapi import FastAPI

from routers import hello_router

app = FastAPI()

app.include_router(
    hello_router
)

if __name__ == "__main__":
    pass
