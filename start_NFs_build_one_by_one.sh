#!/bin/bash

# Usage: ./build_containers.sh <image_name> <app_name>

if [ $# -lt 2 ]; then
    echo "Usage: ./build_containers.sh <image_name> <app_name>"
    exit 1
fi

image_name="$1" # input image name from docker build -t image_name . 
app_name="$2" # app_name is the name of the directory we want to use the dockerfile corresponding to image_name, e.g., amf:1.0.0

case "$app_name" in
    "Dockeramf")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
        #docker run --network hieunetwork --ip 172.18.0.4 --name amf_hieu --link nrf -dit "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        #;;
    "Dockerausf")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
    "Dockernrf")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
        #docker run --network hieunetwork --ip 172.18.0.3 --name nrf_hieu -p 8000:8000 --link mongodb -dit "$image_name:1.0.0" 172.18.0.2 -f "./$app_name/Dockerfile" "./$app_name/"
        #;;
    "Dockernssf")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
    "Dockerpcf")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
    "Dockersmf")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
    "Dockerudm")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
    "Dockerudr")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
    "Dockerupf")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
        #docker run -d --network hieunetwork --ip 172.18.0.5 --name upf_hieu --privileged --link nrf -dit "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        #;;
    "Dockerwebconsole")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
    "Dockergnb")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
    "Dockerue")
        docker build -t "$image_name:1.0.0" -f "./$app_name/Dockerfile" "./$app_name/"
        ;;
         
    *)
        echo "Unknown app: $app_name"
        exit 1
        ;;
esac
