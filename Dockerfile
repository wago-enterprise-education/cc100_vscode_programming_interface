FROM linuxserver/code-server
RUN apt update &&\
    apt install -y python3 &&\
    apt install -y nodejs &&\
    apt install -y npm &&\
    apt install -y python3-pip