FROM python:3.11 as base

FROM base as dev

WORKDIR /code

CMD [ "/bin/bash" ]

FROM dev as release

RUN pip install pipenv
COPY Pipfile* .
RUN pipenv install
COPY . .
RUN pipenv run python manage.py collectstatic --no-input

CMD ["pipenv", "run", "gunicorn", "-b", ":8000", "config.wsgi"]
