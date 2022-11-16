FROM python:3.10

WORKDIR /app

RUN apt update && apt install netcat postgresql-client dnsutils -y

RUN pip install --upgrade pip

# with pip and requirements.txt

 COPY ./requirements.txt /app/ \
        && pip install -r requirements.txt

# with poetry \
# COPY ./pyproject.toml ./poetry.lock* /app/ \
#         && poetry config virtualenvs.create false --local \
#         && poetry config virtualenvs.create false \
#         && poetry config virtualenvs.in-project false --local \
#         && poetry update --no-dev

COPY . .

EXPOSE ${PORT}

COPY ./entrypoint.sh /app/

RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python3", "main.py"]

# Path: entrypoint.sh
#!/bin/sh

