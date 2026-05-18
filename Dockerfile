FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
RUN pip install poetry
WORKDIR /app
COPY . /app
RUN poetry install --without dev --no-root
CMD ["poetry", "run", "python", "src/app.py"]