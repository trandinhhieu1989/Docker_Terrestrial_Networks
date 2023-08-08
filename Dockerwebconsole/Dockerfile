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
    iproute2 \
    gcc \
    vim \
    iputils-ping \
    telnet \
    net-tools \
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

#Install Yarn https://linuxhint.com/install_yarn_ubuntu/
#RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
#RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
#RUN apt install -y yarn
#RUN yarn --version

# Install free5gc
RUN git clone --recursive -b v3.3.0 -j `nproc` https://github.com/free5gc/free5gc.git

RUN apt remove cmdtest
RUN apt remove yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install -y nodejs yarn

WORKDIR /free5gc
RUN make webconsole

WORKDIR /free5gc/webconsole
# COPY from host to docker container in /free5gc
COPY start_webconsole.sh .
# Save the script and make it executable:
RUN chmod +x start_webconsole.sh
ENTRYPOINT ["./start_webconsole.sh"]
