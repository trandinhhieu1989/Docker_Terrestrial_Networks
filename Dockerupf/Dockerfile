#  GNU nano 6.2                               Dockerfile *   
                                  
# Use the official Ubuntu 20.04 base image
FROM ubuntu:22.04
# SHELL ["/bin/bash", "-c"]
# Update the package lists and install required packages
RUN apt-get update && \
    apt-get install -y \
    software-properties-common \
    curl \
    wget \
    build-essential \
    gcc \
    make \
    git \
    vim \
    iputils-ping \
    telnet \
    net-tools \
    linux-headers-$(uname -r) \
    g++ \
    cmake \
    autoconf \
    libtool \
    pkg-config \
    libmnl-dev \
    libyaml-dev \
    golang \
    && mkdir ~/go \
    && export GOPATH=$~/go \
    && export PATH=$PATH:/usr/lib/go/bin:$GOPATH/bin

#RUN go mod tidy    
#RUN go get -u github.com/sirupsen/logrus@latest

#RUN uname -r
 
#RUN apt-get -y update
# RUN go get -u github.com/sirupsen/logrus
#COPY /lib/modules/5.19.0-50-generic/kernel/drivers/net


# Install 5G GTP-U kernel
#RUN git clone https://github.com/PrinzOwO/gtp5g.git
#RUN git clone -b v0.8.1 https://github.com/free5gc/gtp5g.git
#WORKDIR /gtp5g
#RUN git checkout v0.3.2
#RUN make clean
#RUN make
#RUN make install

# Install free5gc upf
RUN git clone --recursive -b v3.3.0 -j `nproc` https://github.com/free5gc/free5gc.git 

WORKDIR /free5gc
RUN make upf

# Follow https://github.com/free5gc/free5gc-stage-3 
#WORKDIR $GOPATH/src/free5gc/src/upf
#RUN make upf
#RUN mkdir build
#WORKDIR /build
#RUN cmake
#RUN make -j`nproc`

