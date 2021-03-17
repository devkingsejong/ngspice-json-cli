FROM ubuntu:18.04
MAINTAINER devkingsejong <devkingsejong@gmail.com>

RUN apt update
RUN apt -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt -y install python3.8
RUN apt -y install git
RUN apt -y install ngspice

RUN git clone -b 0.0.1 https://github.com/devkingsejong/ngspice-json-cli
WORKDIR /ngspice-json-cli
RUN apt -y install python3-pip
RUN python3.8 -m pip install -r ngspicejson/requirements.txt
