FROM python:3.8.10

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV FT_APP_ENV="docker"

RUN mkdir /src/app -p

COPY . /src/app

WORKDIR /src/app


RUN pip install -r requirements.txt

#ENTRYPOINT ["tail", "-f", "/dev/null"]
#CMD ["main.py"]
#ENTRYPOINT ["python3"]

