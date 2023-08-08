#!/bin/bash

# File path of the configuration file where the IP needs to be replaced
NRF_CONFIG=/UERANSIM/config/free5gc-ue.yaml
# Get the IP address of the eth0 interface using the ip command
IP_ADDRESS=$(ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
# IP address that you want to be replaced
GNB_IP=$1

## Using sed to perform the replacement in-place and explaining the command
#sed -i "${LINE_NUMBER}s/127.0.0.10/$IP_ADDRESS/" $CONFIG_FILE

echo "IP address of eth0: $IP_ADDRESS"

sed -i "31s/127.0.0.1/$GNB_IP/" $NRF_CONFIG

# Additional message to indicate the replacement is done
echo "IP address replaced successfully!"


build/nr-ue -c config/free5gc-ue.yaml
