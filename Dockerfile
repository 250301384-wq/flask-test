FROM efreidevopschina.azurecr.io/cache/library/python:3.12-slim
WORKDIR /app
COPY requirements.txt .
COPY app.py .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "test_app.py"]
