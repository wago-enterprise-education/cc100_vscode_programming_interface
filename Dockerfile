#using linuxserver as base image
FROM linuxserver/code-server

RUN apt update &&\
    apt install -y python3 &&\
    apt install -y nodejs &&\
    apt install -y npm &&\
    apt install -y python3-pi

#setting /home as standard directory
WORKDIR /home

#installing latest version of python modul
RUN git clone https://github.com/wago-enterprise-education/wago_cc100_python.git && \
    cd wago_cc100_python/ && \
    pip install . && \
    rm -rf wago_cc100_python

#adding cc100 programming interface
RUN git clone https://github.com/wago-enterprise-education/cc100_programming_interface.git