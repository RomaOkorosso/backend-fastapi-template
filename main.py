from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# from app.routes import name_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(name_router)

# run on app startup events


@app.on_event("startup")
async def startup_event():
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=f"{settings.HOST}", port=settings.PORT)
