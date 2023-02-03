FROM linuxserver/code-server:4.9.1

RUN apt update &&\
    apt install -y python3.10 &&\
    chmod -R 777 /home/

COPY ./PythonModule/* /lib/python3.10/