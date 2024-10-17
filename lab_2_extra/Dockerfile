FROM python:3.12-bookworm

WORKDIR /app
COPY . /lab_2_extra/
RUN pip install --no-cache-dir -r /lab_2_extra/requirements.txt

CMD ["python", "/lab_2_extra/simple_api.py"]
