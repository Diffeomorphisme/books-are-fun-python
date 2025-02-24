FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY ./src/backend /app/src/backend
COPY pyproject.toml /app
COPY uv.lock /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# Run the application.
#CMD ["/.venv/bin/fastapi", "run", "src/backend/main.py", "--port", "3000", "--host", "0.0.0.0"]
ENTRYPOINT [ "uv", "run", "src/backend/index.ts"]