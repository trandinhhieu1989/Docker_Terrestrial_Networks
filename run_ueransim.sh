#!/bin/bash


docker run --network hieunetwork --ip 172.18.0.13 --name gnb_hieu -dit gnb:1.0.0  172.18.0.4

# Activate the virtual environment
source /media/hieu/E/Hieu/Dockerfree5gc_github/Pymongo/venv/bin/activate 
# Add 2nd UE's information into MongoDB
python3 /media/hieu/E/Hieu/Dockerfree5gc_github/Pymongo/Add_UE_general.py imsi-208930000000001 imsi-208930000000002 8baf473f2f8fd09487cccbd7097c6862 8baf473f2f8fd09487cccbd7097c6863

docker run --privileged --network hieunetwork --ip 172.18.0.14 --name ue_hieu -dit ue:1.0.0  172.18.0.13 imsi-208930000000001 8baf473f2f8fd09487cccbd7097c6862
docker run --privileged --network hieunetwork --ip 172.18.0.15 --name ue1_hieu -dit ue:1.0.0 172.18.0.13 imsi-208930000000002 8baf473f2f8fd09487cccbd7097c6863

