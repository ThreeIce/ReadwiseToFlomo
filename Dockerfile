FROM python:3

WORKDIR /usr/src/app

COPY . .

Volume ./data.yml

CMD [ "python", "./main.py" ]

