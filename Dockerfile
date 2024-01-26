FROM python:3

WORKDIR /usr/src/app

COPY ./main.py .

RUN pip install pyyaml

Volume ./data.yml

CMD [ "python", "./main.py" ]

