FROM python:3.13

WORKDIR /api
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENTRYPOINT ["streamlit", "run", "src/frontend/main.py", "--server.port=1234", "--server.address=0.0.0.0"]
