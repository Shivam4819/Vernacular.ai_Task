
FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y pip

RUN mkdir Project

COPY Project ./Project

RUN pip install -r ./Project/requirements.txt

EXPOSE 8000

CMD python3 ./Project/manage.py runserver  0.0.0.0:8000

