#!/media/hieutran/f4f77ea7-e872-d901-70e2-7ea7e872d901/Dockerfree5gc_github/myenv/bin/python3

from pymongo import MongoClient
import gridfs
from bson import ObjectId
from datetime import datetime
from Add_UE_function import Add_UE_function
from Add_UE_function import check_exist_UE
from Update_UE_function import Update_UE_function


import sys

# UE1_ID = sys.argv[1]
# UE2_ID = sys.argv[2]
# permanentID1 = sys.argv[3]
# permanentID2 = sys.argv[4]
#
# print("Argument 1:", UE1_ID)
# print("Argument 2:", UE2_ID)
# print("Argument 1:", permanentID1)
# print("Argument 2:", permanentID2)

# Number of UE
No_UE = 2

## UE ID
UE1_ID  = "imsi-208930000000001"
UE2_ID = "imsi-208930000000002"

UEID_arr = [UE1_ID,UE2_ID]

## permanentID
permanentID1 = "8baf473f2f8fd09487cccbd7097c6862"
permanentID2 = "8baf473f2f8fd09487cccbd7097c6863"

permanentID_arr = [permanentID1,permanentID2]
# Generate the current timestamp
current_timestamp = datetime.now().isoformat()
# Replace "mongodb://localhost:27017" with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017")
# Access a specific database and collection
db = client["free5gc"]
# print(collection)
for i in range(1,No_UE+1):
    collection = db["policyData.ues.amData"]
    document = {}
    # Find the UE_ID and permanentID in UEID_arr and permanentID_arr, respectively
    UE_ID  = UEID_arr[i-1]
    permanent_ID = permanentID_arr[i - 1]
    ## Check UE existence
    check_UE_exist = check_exist_UE(collection,UE_ID,i)
    if check_UE_exist:
        print("UE {} exist".format(i))
        print("Update UE {} information".format(i))
        # Update UEi into MongoDB
        Update_UE = Update_UE_function(UE_ID, permanent_ID,i)
        print("We already update the UEs' information into MongoDB")
    else:
        print("Insert UE {} information".format(i))
        # Add UEi into MongoDB
        Add_UE = Add_UE_function(UE_ID, permanent_ID)
        print("We already insert the UEs' information into MongoDB")

# Close the MongoDB connection
client.close()


# Define a new function is non empty list
# def check_exist_UE(collection,UE_ID):
#     exist = 0
#     ## Write a function to check the existence of UE in mongoDB
#     # Find the document that contains the specified value
#     document = collection.find_one({"ueId": UE_ID})
#     # Check if the document exists or not. If it exists in the MongoDB, we update the new information and overwrite the old one
#     # Otherwise, we insert the new information into Mongodb
#     if document:
#         print("Document found:", document)
#         print("Update UE {} information".format(i))
#         exist = 1
#     else:
#         print("Ue {} not found for the specified value".format(i))
#         print("Insert UE {} information".format(i))
#     return exist
