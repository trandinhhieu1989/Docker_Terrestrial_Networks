#!/bin/bash

# File path of the configuration file where the IP needs to be replaced
NRF_CONFIG=/free5gc/config/nssfcfg.yaml
# Get the IP address of the eth0 interface using the ip command
IP_ADDRESS=$(ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
# IP address that you want to be replaced
NRF_IP=$1 #192.168.1.61


## Using sed to perform the replacement in-place and explaining the command
#sed -i "${LINE_NUMBER}s/127.0.0.10/$IP_ADDRESS/" $CONFIG_FILE

#sed -i "7s/127.0.0.1/$MONGO_IP/" $NRF_CONFIG

echo "IP address of eth0: $IP_ADDRESS"

sed -i "9s/127.0.0.31/$IP_ADDRESS/" $NRF_CONFIG
sed -i "10s/127.0.0.31/$IP_ADDRESS/" $NRF_CONFIG
sed -i "18s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "42s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "49s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "56s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "58s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "65s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "71s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "78s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "85s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "92s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "101s/127.0.0.10/$NRF_IP/" $NRF_CONFIG
sed -i "129s/localhost/$NRF_IP/" $NRF_CONFIG
# Additional message to indicate the replacement is done
echo "IP address replaced successfully!"

./bin/nssf
