FROM python:3

WORKDIR /usr/src/app

RUN pip install pyyaml \
    && pip install requests

COPY ./main.py .

Volume ./data.yml

CMD [ "python", "./main.py" ]

