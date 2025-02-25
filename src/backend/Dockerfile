FROM python:3.13-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY ./src/backend /app/src/backend
COPY requirements.txt /app

# Install the application dependencies.
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the application.
#CMD ["/.venv/bin/fastapi", "run", "src/backend/main.py", "--port", "3000", "--host", "0.0.0.0"]
CMD uvicorn src.backend.main:app --proxy-headers --host 0.0.0.0 --port 3000
