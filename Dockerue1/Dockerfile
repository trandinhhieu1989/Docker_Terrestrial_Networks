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
    git \
    gcc \
    vim \
    iputils-ping \
    telnet \
    net-tools \
    make \
    g++ \
    cmake \
    iproute2 \
    autoconf \
    libtool \
    pkg-config \
    libsctp-dev \
    lksctp-tools \
    libmnl-dev \
    libyaml-dev \
    golang \
    && mkdir ~/go \
    && export GOPATH=$~/go \
    && export PATH=$PATH:/usr/lib/go/bin:$GOPATH/bin

# Install ueransim
RUN git clone https://github.com/aligungr/UERANSIM

WORKDIR /UERANSIM
RUN make

# COPY from host to docker container in /ueransim
COPY start_ue1.sh .
COPY free5gc-ue.yaml  config/
# Save the script and make it executable:
RUN chmod +x start_ue1.sh
ENTRYPOINT ["./start_ue1.sh"]
