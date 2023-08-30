#!/bin/bash


docker run --network hieunetwork --ip 172.18.0.13 --name gnb_hieu -dit gnb:1.0.0  172.18.0.4

# Output imsi's values from config.yaml file. Use yq to extract the values from the YAML file
# Full path to the yq executable
YQ_EXECUTABLE="/usr/local/bin/yq"
imsi_values=$("$YQ_EXECUTABLE" eval '.imsi[]' /media/hieu/E/Hieu/Dockerfree5gc_github/config.yaml)
#imsi_values=$(grep -A 1000 "imsi:" /media/hieu/E/Hieu/Dockerfree5gc_github/config.yaml | grep -E "^  - imsi-" | awk '{print $2}')
# Split the values into an array
IFS=$'\n' read -r -d '' -a imsi_value_array <<< "$imsi_values"

# Assign values to separate variables
imsi_1="${imsi_value_array[0]}"
imsi_2="${imsi_value_array[1]}"
# Print the values
echo "imsi 1: $imsi_1"
echo "imsi 2: $imsi_2"
# Output key's values from config.yaml file
key_values=$(yq eval '.key[]' config.yaml)
# Split the values into an array
IFS=$'\n' read -r -d '' -a key_value_array <<< "$key_values"

# Assign values to separate variables
key_1="${key_value_array[0]}"
key_2="${key_value_array[1]}"
# Print the values
echo "key 1: $key_1"
echo "key 2: $key_2"

# Activate the virtual environment
source /media/hieu/E/Hieu/Dockerfree5gc_github/Pymongo/venv/bin/activate 
# Add 2nd UE's information into MongoDB
python3 /media/hieu/E/Hieu/Dockerfree5gc_github/Pymongo/Add_UE_general.py $imsi_1 $imsi_2 $key_1 $key_2

docker run --privileged --network hieunetwork --ip 172.18.0.14 --name ue_hieu -dit ue:1.0.0  172.18.0.13 imsi-208930000000001 8baf473f2f8fd09487cccbd7097c6862
docker run --privileged --network hieunetwork --ip 172.18.0.15 --name ue1_hieu -dit ue:1.0.0 172.18.0.13 imsi-208930000000002 8baf473f2f8fd09487cccbd7097c6863

