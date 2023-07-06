FROM linuxserver/code-server
#FROM linuxserver/code-server:arm32v7-latest

RUN apt update &&\
    apt install -y python3 &&\
    apt install -y nodejs &&\
    apt install -y npm &&\
    apt install -y python3-pip

WORKDIR /home

# install python module for CC100
RUN git clone https://github.com/wago-enterprise-education/wago_cc100_python.git && \
    cd wago_cc100_python/ && \
    pip install . && \
    rm -rf wago_cc100_python/

# install cc100 programming interface
RUN git clone https://github.com/wago-enterprise-education/cc100_programming_interface.git


# add python extension to vs code
ENV VSCODE_EXTENSION_IDS="ms-python.python"

# start cc100 programming interface
CMD [ "npm", "start", "--prefix", "cc100_programming_interface/server/" ]
