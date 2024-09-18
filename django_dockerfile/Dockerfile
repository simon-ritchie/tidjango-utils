FROM python:3.12.6-bullseye
ARG WORKDIR=/mnt/tidjango-serverless-utils/
RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
ADD requirements.txt ${WORKDIR}
RUN pip install -r requirements.txt
RUN apt update
RUN apt install sudo
RUN apt install python3-dev -y
RUN apt install default-libmysqlclient-dev -y
RUN apt install build-essential -y
RUN apt install pkg-config -y
RUN apt install mariadb-client -y
RUN apt install vim -y
RUN echo "set mouse-=a" >> ~/.vimrc
