#!/bin/bash

# Usage:  ./build_NFs.sh <image_name> <app_name>


docker build -t "nrf:1.0.0" -f "./Dockernrf/Dockerfile" "./Dockernrf/"
docker build -t "amf:1.0.0" -f "./Dockeramf/Dockerfile" "./Dockeramf/"
docker build -t "upf:1.0.0" -f "./Dockerupf/Dockerfile" "./Dockerupf/"
docker build -t "smf:1.0.0" -f "./Dockersmf/Dockerfile" "./Dockersmf/"
docker build -t "ausf:1.0.0" -f "./Dockerausf/Dockerfile" "./Dockerausf/"
docker build -t "nssf:1.0.0" -f "./Dockernssf/Dockerfile" "./Dockernssf/"
docker build -t "pcf:1.0.0" -f "./Dockerpcf/Dockerfile" "./Dockerpcf/"
docker build -t "udm:1.0.0" -f "./Dockerudm/Dockerfile" "./Dockerudm/"
docker build -t "udr:1.0.0" -f "./Dockerudr/Dockerfile" "./Dockerudr/"
docker build -t "webconsole:1.0.0" -f "./Dockerwebconsole/Dockerfile" "./Dockerwebconsole/"
docker build -t "gnb:1.0.0" -f "./Dockergnb/Dockerfile" "./Dockergnb/"
docker build -t "ue:1.0.0" -f "./Dockerue/Dockerfile" "./Dockerue/"
