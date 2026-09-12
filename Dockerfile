FROM python:3.12-slim
WORKDIR /app
COPY saudacao.py .
CMD ["python", "saudacao.py"]