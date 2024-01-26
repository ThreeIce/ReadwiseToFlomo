FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install pyyaml \
    &&

Volume ./data.yml

CMD [ "python", "./main.py" ]

