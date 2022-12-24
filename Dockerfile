FROM python:3.11 as base

FROM base as dev

WORKDIR /tmp
RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/download/v3.2.4/tailwindcss-linux-x64
RUN chmod +x tailwindcss-linux-x64
RUN mv tailwindcss-linux-x64 /usr/local/bin/tailwindcss

WORKDIR /code

CMD [ "/bin/bash" ]

FROM dev as release

RUN pip install pipenv
COPY Pipfile* .
RUN pipenv install
COPY . .
RUN tailwindcss -i static/src/css/index.css -o static/dist/css/index.css --minify
RUN pipenv run python manage.py collectstatic --no-input --settings config.settings.collectstatic

CMD ["pipenv", "run", "gunicorn", "-b", ":8000", "config.wsgi"]
