#!/bin/bash

# File path of the configuration file where the IP needs to be replaced
NRF_CONFIG=/free5gc/config/upfcfg.yaml
# Get the IP address of the eth0 interface using the ip command
IP_ADDRESS=$(ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
# IP address that you want to be replaced
#NRF_IP=$1

## Using sed to perform the replacement in-place and explaining the command
#sed -i "${LINE_NUMBER}s/127.0.0.10/$IP_ADDRESS/" $CONFIG_FILE

echo "IP address of eth0: $IP_ADDRESS"

sed -i "6s/127.0.0.8/$IP_ADDRESS/" $NRF_CONFIG
sed -i "7s/127.0.0.8/$IP_ADDRESS/" $NRF_CONFIG
sed -i "16s/127.0.0.8/$IP_ADDRESS/" $NRF_CONFIG

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

#sed -i "46s/127.0.0.10/$NRF_IP/" $NRF_CONFIG

# Additional message to indicate the replacement is done
echo "IP address replaced successfully!"

./bin/upf
