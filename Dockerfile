FROM python:3

WORKDIR /usr/src/app

COPY ./main.py .

RUN pip install pyyaml \
    && pip install requests

Volume ./data.yml

CMD [ "python", "./main.py" ]

