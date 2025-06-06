FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    gcc \
    g++ 

RUN pip install --no-cache-dir -r requirements.txt

RUN huggingface-cli download sentence-transformers/all-MiniLM-L6-v2

RUN python -m spacy download en_core_web_sm

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "-m", "unittest", "discover", "-s", "app/tests"]

