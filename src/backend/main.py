from fastapi import FastAPI

from src.backend.routes import books_router


app = FastAPI(
    title="Books Are Fun Python",
)
app.include_router(books_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        'main:src',
        host='0.0.0.0',
        port=3000,
        log_level='info',
        reload=False
    )
