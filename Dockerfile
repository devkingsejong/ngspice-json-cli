FROM ubuntu:18.04

RUN apt update
RUN apt -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt -y install python3.8
RUN apt -y install python3.8-dev
RUN apt -y install ngspice

COPY . /ngspice-json-cli
WORKDIR /ngspice-json-cli
RUN apt -y install python3-pip
RUN python3.8 -m pip install --upgrade pip setuptools
RUN python3.8 -m pip install -r ngspicejson/requirements.txt

CMD sh run_server.sh & tail -f /dev/null
EXPOSE 15781
