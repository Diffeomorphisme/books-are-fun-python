from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.backend.routes import api_router

origins = [
    "http://localhost:1234",
    "https://127.0.0.1:1234",
    "http://0.0.0.0:1234",
]

app = FastAPI(
    title="Books Are Fun Python",
)
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=3000,
        log_level='info',
        reload=False
    )
