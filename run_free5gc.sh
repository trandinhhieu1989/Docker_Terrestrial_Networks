#!/bin/bash 

# Create a Docker network to connect all containers
docker network create --subnet=172.18.0.0/16 hieunetwork

docker run --name mongodb --ip 172.18.0.2 --network hieunetwork -p 27017:27017 -dit mongo:latest

docker run --network hieunetwork --ip 172.18.0.3 --name nrf_hieu -p 8000:8000 -dit nrf:1.0.0 172.18.0.2 
docker run --network hieunetwork --ip 172.18.0.4 --name amf_hieu -dit amf:1.0.0 172.18.0.3
docker run --privileged --network hieunetwork --ip 172.18.0.5 --name upf_hieu -dit upf:1.0.0
docker run --network hieunetwork --ip 172.18.0.6 --name smf_hieu -dit smf:1.0.0 172.18.0.3 172.18.0.5
docker run --network hieunetwork --ip 172.18.0.7 --name ausf_hieu -dit ausf:1.0.0 172.18.0.3
docker run --network hieunetwork --ip 172.18.0.8 --name nssf_hieu -dit nssf:1.0.0 172.18.0.3 
docker run --network hieunetwork --ip 172.18.0.9 --name pcf_hieu -dit pcf:1.0.0 172.18.0.2 172.18.0.3 
docker run --network hieunetwork --ip 172.18.0.10 --name udm_hieu -dit udm:1.0.0 172.18.0.3 
docker run --network hieunetwork --ip 172.18.0.11 --name udr_hieu -dit udr:1.0.0 172.18.0.2 172.18.0.3 

#docker run --network hieunetwork --ip 172.18.0.12 --name webconsole_hieu -it webconsole:1.0.0 172.18.0.2 bash


# Activate the virtual environment
#source /media/hieu/E/Hieu/Dockerfree5gc_github/Pymongo/venv/bin/activate
# Add 2nd UE's information into MongoDB
#python3 /media/hieu/E/Hieu/Dockerfree5gc_github/Pymongo/Add_UE_general.py 
