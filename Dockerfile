FROM python:3.11-slim-bullseye
LABEL maintainer="jamesaglynn10@gmail.com"
LABEL version="0.8"
LABEL description="Docker image for deployment to production for Roman Emperors Project"

ENV PRODUCTION=true

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -yq tzdata
RUN ln -fs /usr/share/zoneinfo/Australia/Sydney /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata

ENV TZ="Australia/Sydney"

WORKDIR /home/re/

COPY static /home/re/static
COPY templates /home/re/templates
COPY principale.py /home/re/principale.py
COPY requirements.txt /home/re/requirements.txt

RUN python3 -m pip install --upgrade -r /home/re/requirements.txt

EXPOSE 80 443

CMD ["python3", "/home/re/principale.py"]