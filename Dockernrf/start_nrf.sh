#!/bin/bash

NRF_CONFIG=/free5gc/config/nrfcfg.yaml
# Get the IP address of the eth0 interface using the ip command
IP_ADDRESS=$(ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
MONGO_IP=$1

sed -i "7s/127.0.0.1/$MONGO_IP/" $NRF_CONFIG

echo "IP address of eth0: $IP_ADDRESS"

sed -i "10s/127.0.0.10/$IP_ADDRESS/" $NRF_CONFIG
sed -i "11s/127.0.0.10/$IP_ADDRESS/" $NRF_CONFIG

./bin/nrf
