FROM python:3.11 as base

FROM base as dev

WORKDIR /code

CMD [ "/bin/bash" ]
