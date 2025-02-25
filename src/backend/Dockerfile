FROM python:3.13-slim

# Copy the application into the container.
COPY ./src/backend /app/src/backend
COPY requirements.txt /app

# Install the application dependencies.
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Run the application.
CMD uvicorn src.backend.main:app --proxy-headers --host 0.0.0.0 --port 3000

# To do - optimise to minimise the size of the image