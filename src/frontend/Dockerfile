FROM python:3.13-slim

# Copy the application into the container.
COPY ./src/frontend app/src/frontend
COPY requirements.txt /app

# Install the application dependencies.
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Run the application.
CMD streamlit run --server.port 1234 --server.address 0.0.0.0 src/frontend/main.py
