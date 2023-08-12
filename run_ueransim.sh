#!/bin/bash


docker run --network hieunetwork --ip 172.18.0.13 --name gnb_hieu -dit gnb:1.0.0  172.18.0.4
docker run --privileged --network hieunetwork --ip 172.18.0.14 --name ue_hieu -dit ue:1.0.0  172.18.0.13

