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
    vim \
    net-tools \
    iputils-ping \
    telnet \
    git \
    linux-headers-$(uname -r) \
    gcc \
    iproute2 \
    iptables \
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

# Install free5gc
RUN git clone --recursive -b v3.3.0 -j `nproc` https://github.com/free5gc/free5gc.git 

WORKDIR /free5gc
RUN make upf

# COPY from host to docker container in /free5gc
COPY start_upf.sh .
# Save the script and make it executable:
RUN chmod +x start_upf.sh
ENTRYPOINT ["./start_upf.sh"]
