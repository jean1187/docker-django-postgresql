FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD codegis_access/requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

#docker-compose run web mkdir logs
#docker-compose run web touch logs/codegis_access.log
#docker-compose run web bash
