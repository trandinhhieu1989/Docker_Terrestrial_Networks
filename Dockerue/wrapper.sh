#!/bin/bash

mkdir /dev/net
mknod /dev/net/tun c 10 200
./nr-ue -c ../config/free5gc-ue.yaml
ping -I uesimtun0 google.com
