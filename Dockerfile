FROM python:3.8

RUN pip install poetry && poetry config virtualenvs.create false

RUN mkdir /paypay

COPY poetry.lock pyproject.toml alembic.ini .env /paypay/

WORKDIR /paypay

RUN poetry install --no-interaction

COPY src/ /paypay/src

ENV PYTHONPATH /paypay:/paypay/src

CMD ["python3", "src/paypay/entrypoint/http/main.py"]