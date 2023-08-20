# Docker_NTN
In this project, we try to solve many exercises to building a 5G network.
1. Build 5G core, RAN, and UE using Dockerfile. Specifically, we used open sources such as free5gc and UERANSIM to build 5g core and RAN/UE, respectively. Each NF in free5gc, RAN, and UE are built as a separeate docker container.
2. Using Bashscript to update the IP address of each NF in free5gc, RAN, and UE automatically.
3. Build all network functions (NFs) in free5gc and UERANSIM using build_NFs.sh.
4. Run all NFs in free5gc and UERANSIM using run_free5gc.sh and run_ueransim.sh, respectively.
5. In Pymongo folder, I create a script to update all the subscriber registration automatically instead of running manually using webconsole as in step 4 of https://free5gc.org/guide/5-install-ueransim/#3-install-free5gc-webconsole 


