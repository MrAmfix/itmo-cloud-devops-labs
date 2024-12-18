FROM python:3.12-bookworm

WORKDIR /app
COPY requirements.txt simple_api.py tests.py /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "simple_api:app", "--host", "0.0.0.0", "--port", "8000"]
