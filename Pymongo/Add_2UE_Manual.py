#!/media/hieutran/f4f77ea7-e872-d901-70e2-7ea7e872d901/Dockerfree5gc_github/myenv/bin/python3

from pymongo import MongoClient
import gridfs
from bson import ObjectId
from datetime import datetime

# Number of UE
No_UE = 2
# UE ID
UE1_ID  = "imsi-208930000000001"
UE2_ID = "imsi-208930000000002"

# permanentID
permanentID1 = "8baf473f2f8fd09487cccbd7097c6862"
permanentID2 = "8baf473f2f8fd09487cccbd7097c6863"
# Generate the current timestamp
current_timestamp = datetime.now().isoformat()
# Replace "mongodb://localhost:27017" with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017")

# Access a specific database and collection
db = client["free5gc"]

# Insert the file into GridFS, You use the fs.put() method to insert the file contents into the GridFS. This returns a unique file ID.
# file_id = fs.put(file_contents, filename="UE_info_config_file.txt")

# Insert a document into a collection polictyData_ues_amData.json referencing the file
collection = db["policyData.ues.amData"]
# polictyData_ues_amData.json data to be inserted into the collections
Policy_data_am = [
    {"_id":  ObjectId(), "subscCats": ["free5gc"], "ueId": UE1_ID},
    {"_id":  ObjectId(), "subscCats": ["free5gc"], "ueId": UE2_ID }
]
# Insert the data into the collections
if No_UE==1:
    res = collection.insert_one(Policy_data_am)
else:
    res = collection.insert_many(Policy_data_am)

# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record = collection.find_one()
# Print the retrieved document
print(record)
###########################################################################
# Insert a document into a collection polictyData_ues_amData.json referencing the file
collection1 = db["policyData.ues.smData"]
# policyData.ues.smData
Policy_data_sm = [
    {  "_id": ObjectId(),
        "smPolicySnssaiData": {
            "01112233": {
                "snssai": {"sst": 1.0, "sd": "112233"},
                "smPolicyDnnData": {
                    "internet": {"dnn": "internet"},
                    "internet2": {"dnn": "internet2"}
                }
            },
            "01010203": {
                "snssai": {"sst": 1.0, "sd": "010203"},
                "smPolicyDnnData": {
                    "internet": {"dnn": "internet"},
                    "internet2": {"dnn": "internet2"}
                }
            }
        },
        "ueId": UE1_ID
    },
    {
        "_id": ObjectId(),
        "smPolicySnssaiData": {
            "01010203": {
                "snssai": {"sst": 1.0, "sd": "010203"},
                "smPolicyDnnData": {
                    "internet": {"dnn": "internet"},
                    "internet2": {"dnn": "internet2"}
                }
            },
            "01112233": {
                "snssai": {"sst": 1.0, "sd": "112233"},
                "smPolicyDnnData": {
                    "internet": {"dnn": "internet"},
                    "internet2": {"dnn": "internet2"}
                }
            }
        },
        "ueId": UE2_ID
    }
]
# Insert the data into the collections
if No_UE==1:
    res1 = collection1.insert_one(Policy_data_sm)
    print(res1.inserted_id)
else:
    res1 = collection1.insert_many(Policy_data_sm)
    print(res1.inserted_ids)

# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record1 = collection1.find_one()
# Print the retrieved document
print(record1)
###########################################################################
collection2 = db["subscriptionData.authenticationData.authenticationStatus"]
# Json Data
subsData_auth_Status = [
    { "_id": ObjectId(), "nfInstanceId": "9ff8ef58-cdc2-4001-971f-d98dcb9ec81f",
        "success": True, "timeStamp": current_timestamp, "authType": "5G_AKA",
        "servingNetworkName": "5G:mnc093.mcc208.3gppnetwork.org",
        "ueId": UE1_ID
    },
    {
        "_id": ObjectId(), "ueId": UE2_ID,
        "nfInstanceId": "9ff8ef58-cdc2-4001-971f-d98dcb9ec81f",
        "success": True, "timeStamp": current_timestamp, "authType": "5G_AKA",
        "servingNetworkName": "5G:mnc093.mcc208.3gppnetwork.org"
    }
]
# Insert the data into the collections
if No_UE==1:
    res2 = collection2.insert_one(subsData_auth_Status)
    # Print the inserted document's _id
    print(res2.inserted_id)
else:
    res2 = collection2.insert_many(subsData_auth_Status)
    # Print the inserted document's _id
    print(res2.inserted_ids)

# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record2 = collection2.find_one()
# Print the retrieved document
print(record2)
###########################################################################
#
collection3 = db["subscriptionData.authenticationData.authenticationSubscription"]
# Json Data
subsData_auth = [
    {
        "_id": ObjectId(), "sequenceNumber": "000000000022","authenticationManagementField": "8000",
        "milenage": {  "op": { "encryptionAlgorithm": 0.0, "encryptionKey": 0.0, "opValue": "" }    },
        "opc": { "encryptionAlgorithm": 0.0, "encryptionKey": 0.0, "opcValue": "8e27b6af0e692e750f32667a3b14605d" },
        "ueId": UE1_ID, "authenticationMethod": "5G_AKA",
        "permanentKey": {"permanentKeyValue": permanentID1 ,"encryptionAlgorithm": 0.0,"encryptionKey": 0.0 }
    },
    {
        "_id": ObjectId(), "authenticationMethod": "5G_AKA",
        "permanentKey": {"encryptionAlgorithm": 0.0,"encryptionKey": 0.0, "permanentKeyValue": permanentID2 },
        "sequenceNumber": "000000000022", "authenticationManagementField": "8000",
        "milenage": { "op": { "encryptionAlgorithm": 0.0, "encryptionKey": 0.0, "opValue": ""  }     },
        "opc": { "opcValue": "8e27b6af0e692e750f32667a3b14605d", "encryptionAlgorithm": 0.0, "encryptionKey": 0.0  },
        "ueId": UE2_ID
    }
]
# Insert the data into the collections
if No_UE==1:
    res3 = collection3.insert_one(subsData_auth)
    # Print the inserted document's _id
    print(res3.inserted_id)
else:
    res3 = collection3.insert_many(subsData_auth)
    # Print the inserted document's _id
    print(res3.inserted_ids)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record3 = collection3.find_one()
# Print the retrieved document
print(record3)
###########################################################################

collection4 = db["subscriptionData.authenticationData.authenticationSubscription"]
# Json Data
amf3gpp = [
    {
        "_id": ObjectId(), "ratType": "", "ueId": UE1_ID,
        "amfInstanceId": "d491a3cd-386c-45f3-ab2a-49c916f21b3d",
        "imsVoPs": "HOMOGENEOUS_NON_SUPPORT", "deregCallbackUri": "",
        "initialRegistrationInd": True,
        "guami": { "plmnId": {"mcc": "208", "mnc": "93"}, "amfId": "cafe00" }  },
    {
        "_id": ObjectId(), "deregCallbackUri": "", "initialRegistrationInd": True,
        "guami": { "plmnId": {"mcc": "208", "mnc": "93"}, "amfId": "cafe00" },
        "ratType": "",
        "ueId": UE2_ID,
        "amfInstanceId": "d491a3cd-386c-45f3-ab2a-49c916f21b3d",
        "imsVoPs": "HOMOGENEOUS_NON_SUPPORT"
    }
]
# Insert the data into the collections
if No_UE==1:
    res4 = collection4.insert_one(amf3gpp)
    # Print the inserted document's _id
    print(res4.inserted_id)
else:
    res4 = collection4.insert_many(amf3gpp)
    # Print the inserted document's _id
    print(res4.inserted_ids)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record4 = collection4.find_one()
# Print the retrieved document
print(record4)
###########################################################################
collection = db["subscriptionData.provisionedData.amData"]
# Json Data
subsData_provision_am = [
    {
        "_id": ObjectId(),
        "gpsis": ["msisdn-"],
        "subscribedUeAmbr": {"uplink": "1 Gbps", "downlink": "2 Gbps"},
        "nssai": {
            "defaultSingleNssais": [ {"sst": 1.0, "sd": "010203"}, {"sst": 1.0, "sd": "112233"}  ]    },
        "ueId": UE1_ID,
        "servingPlmnId": "20893"
    },
    {
        "_id": ObjectId(),
        "gpsis": ["msisdn-"],
        "subscribedUeAmbr": {"uplink": "1 Gbps", "downlink": "2 Gbps"},
        "nssai": { "defaultSingleNssais": [ {"sst": 1.0, "sd": "010203"}, {"sst": 1.0, "sd": "112233"} ] },
        "ueId": UE2_ID,
        "servingPlmnId": "20893"
    }
]
# Insert the data into the collections
if No_UE==1:
    res5 = collection.insert_one(subsData_provision_am)
    # Print the inserted document's _id
    print(res5.inserted_id)
else:
    res5 = collection.insert_many(subsData_provision_am)
    # Print the inserted document's _id
    print(res5.inserted_ids)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record5 = collection.find_one()
# Print the retrieved document
print(record5)

###########################################################################
collection = db["subscriptionData.provisionedData.smData"]
# Json Data
subsData_provision_sm = [
    {
        "_id": ObjectId(),
        "singleNssai": {"sd": "010203", "sst": 1.0},
        "dnnConfigurations": {
            "internet": {
                "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
                "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
                "5gQosProfile": {"5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}, "priorityLevel": 8.0},
                "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"}
            },
            "internet2": {
                "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
                "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
                "5gQosProfile": {"priorityLevel": 8.0, "5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}},
                "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"}
            }
        },
        "ueId": UE1_ID,
        "servingPlmnId": "20893"
    },
    {
        "_id": ObjectId(),
        "singleNssai": {"sst": 1.0, "sd": "112233"},
        "dnnConfigurations": {
            "internet2": {
                "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
                "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
                "5gQosProfile": {"priorityLevel": 8.0, "5qi": 9.0, "arp": {"preemptCap": "", "preemptVuln": "", "priorityLevel": 8.0}},
                "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"}
            },
            "internet": {
                "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"},
                "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
                "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
                "5gQosProfile": {"5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}, "priorityLevel": 8.0}
            }
        },
        "ueId": UE1_ID,
        "servingPlmnId": "20893"
    },
    {
        "_id": ObjectId(),
        "singleNssai": {"sst": 1.0, "sd": "010203"},
        "dnnConfigurations": {
            "internet": {
                "5gQosProfile": {"5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}, "priorityLevel": 8.0},
                "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"},
                "pduSessionTypes": {"allowedSessionTypes": ["IPV4"], "defaultSessionType": "IPV4"},
                "sscModes": {"allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"], "defaultSscMode": "SSC_MODE_1"}
            },
            "internet2": {
                "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
                "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
                "5gQosProfile": {"priorityLevel": 8.0, "5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}},
                "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"}
            }
        },
        "ueId": UE2_ID,
        "servingPlmnId": "20893"
    },
    {
        "_id": ObjectId(),
        "ueId": UE2_ID,
        "servingPlmnId": "20893",
        "singleNssai": {"sst": 1.0, "sd": "112233"},
        "dnnConfigurations": {
            "internet": {
                "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"},
                "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
                "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
                "5gQosProfile": {"5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}, "priorityLevel": 8.0}
            },
            "internet2": {
                "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
                "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
                "5gQosProfile": {"5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}, "priorityLevel": 8.0},
                "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"}
            }
        }
    }
]
# Insert the data into the collections
res6 = collection.insert_many(subsData_provision_sm)
# Print the inserted document's _id
print(res6.inserted_ids)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record6 = collection.find_one()
# Print the retrieved document
print(record6)
###########################################################################
collection = db["subscriptionData.provisionedData.smfSelectionSubscriptionData"]
# Json Data
subsData_provision_smf = [
    {
        "_id": ObjectId(),
        "subscribedSnssaiInfos": {
            "01010203": {
                "dnnInfos": [ {"dnn": "internet"}, {"dnn": "internet2"}
                ]
            },
            "01112233": {
                "dnnInfos": [ {"dnn": "internet"}, {"dnn": "internet2"}  ]  }
        },
        "ueId": UE1_ID,
        "servingPlmnId": "20893"
    },
    {
        "_id": ObjectId(),
        "subscribedSnssaiInfos": {
            "01010203": {
                "dnnInfos": [ {"dnn": "internet"}, {"dnn": "internet2"}
                ]
            },
            "01112233": {
                "dnnInfos": [ {"dnn": "internet"},  {"dnn": "internet2"}  ]   }
        },
        "ueId": UE2_ID,
        "servingPlmnId": "20893"
    }
]

# Insert the data into the collections
if No_UE==1:
    res7 = collection.insert_one(subsData_provision_smf)
    # Print the inserted document's _id
    print(res7.inserted_id)
else:
    res7 = collection.insert_many(subsData_provision_smf)
    print(res7.inserted_ids)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record7 = collection.find_one()
# Print the retrieved document
print(record7)

print("we already insert the second UE's information into MongoDB")
# Close the MongoDB connection
client.close()
