#!/media/hieutran/f4f77ea7-e872-d901-70e2-7ea7e872d901/Dockerfree5gc_github/myenv/bin/python3

from pymongo import MongoClient
import gridfs
from bson import ObjectId
from datetime import datetime
#
## CHeck the existence of an UE in MongoDB
def check_exist_UE(collection,UE_ID,i):
    exist = 0
    ## Write a function to check the existence of UE in mongoDB
    # Find the document that contains the specified value
    document = collection.find_one({"ueId": UE_ID})
    # Check if the document exists or not. If it exists in the MongoDB, we update the new information and overwrite the old one
    # Otherwise, we insert the new information into Mongodb
    if document:
        exist = 1
    else:
        print("Ue {} not found for the specified value".format(i))
    return exist

## Insert UE's information into MongoDB
def Add_UE_function(UE_ID,permanentID):
    # Generate the current timestamp
    current_timestamp = datetime.now().isoformat()
    # Replace "mongodb://localhost:27017" with your MongoDB connection string
    client = MongoClient("mongodb://localhost:27017")

    # Access a specific database and collection
    db = client["free5gc"]

    # Insert a document into a collection polictyData_ues_amData.json referencing the file
    collection = db["policyData.ues.amData"]
    # polictyData_ues_amData.json data to be inserted into the collections
    Policy_data_am =  {"_id":  ObjectId(), "subscCats": ["free5gc"], "ueId": UE_ID}
    # Insert the data into the collections
    res = collection.insert_one(Policy_data_am)
    # print(res.inserted_id)
    # Step 7: Reading the document that we insert. Retrieve a single document from the collection
    record = collection.find_one()
    # Print the retrieved document
    print("policyData.ues.amData",record)
    ###########################################################################
    # Insert a document into a collection polictyData_ues_amData.json referencing the file
    collection1 = db["policyData.ues.smData"]
    # policyData.ues.smData
    Policy_data_sm = {
        "_id": ObjectId(),
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
            "ueId": UE_ID
        }
    # Insert the data into the collections
    res1 = collection1.insert_one(Policy_data_sm)
    # print(res1.inserted_id)
    #
    # # Print the names of all databases on the MongoDB server
    # print("Database Names:", client.list_database_names())
    # Step 7: Reading the document that we insert. Retrieve a single document from the collection
    record1 = collection1.find_one()
    # Print the retrieved document
    print("policyData.ues.smData",record1)
    ###########################################################################
    collection2 = db["subscriptionData.authenticationData.authenticationStatus"]
    # Json Data
    subsData_auth_Status = { "_id": ObjectId(), "nfInstanceId": "9ff8ef58-cdc2-4001-971f-d98dcb9ec81f",
            "success": True, "timeStamp": current_timestamp, "authType": "5G_AKA",
            "servingNetworkName": "5G:mnc093.mcc208.3gppnetwork.org",
            "ueId": UE_ID
        }
    # Insert the data into the collections
    res2 = collection2.insert_one(subsData_auth_Status)
    # Print the inserted document's _id
    # print(res2.inserted_id)
    #
    # # Print the names of all databases on the MongoDB server
    # print("Database Names:", client.list_database_names())
    # Step 7: Reading the document that we insert. Retrieve a single document from the collection
    record2 = collection2.find_one()
    # Print the retrieved document
    print("subscriptionData.authenticationData.authenticationStatus",record2)
    ###########################################################################
    #
    collection3 = db["subscriptionData.authenticationData.authenticationSubscription"]
    # Json Data
    subsData_auth = {
            "_id": ObjectId(), "sequenceNumber": "000000000022","authenticationManagementField": "8000",
            "milenage": {  "op": { "encryptionAlgorithm": 0.0, "encryptionKey": 0.0, "opValue": "" }    },
            "opc": { "encryptionAlgorithm": 0.0, "encryptionKey": 0.0, "opcValue": "8e27b6af0e692e750f32667a3b14605d" },
            "ueId": UE_ID, "authenticationMethod": "5G_AKA",
            "permanentKey": {"permanentKeyValue": permanentID ,"encryptionAlgorithm": 0.0,"encryptionKey": 0.0 }
        }

    # Insert the data into the collections
    res3 = collection3.insert_one(subsData_auth)
    # Print the inserted document's _id
    # print(res3.inserted_id)
    # # Print the names of all databases on the MongoDB server
    # print("Database Names:", client.list_database_names())
    # Step 7: Reading the document that we insert. Retrieve a single document from the collection
    record3 = collection3.find_one()
    # Print the retrieved document
    print("subscriptionData.authenticationData.authenticationSubscription",record3)
    ###########################################################################

    collection4 = db["subscriptionData.contextData.amf3gppAccess"]
    # Json Data
    amf3gpp =  {
            "_id": ObjectId(), "ratType": "", "ueId": UE_ID,
            "amfInstanceId": "d491a3cd-386c-45f3-ab2a-49c916f21b3d",
            "imsVoPs": "HOMOGENEOUS_NON_SUPPORT", "deregCallbackUri": "",
            "initialRegistrationInd": True,
            "guami": { "plmnId": {"mcc": "208", "mnc": "93"}, "amfId": "cafe00" }  }
    # Insert the data into the collections
    res4 = collection4.insert_one(amf3gpp)
    # Print the inserted document's _id
    # print(res4.inserted_id)

    # Print the names of all databases on the MongoDB server
    # print("Database Names:", client.list_database_names())
    # Step 7: Reading the document that we insert. Retrieve a single document from the collection
    record4 = collection4.find_one()
    # Print the retrieved document
    print("subscriptionData.contextData.amf3gppAccess",record4)
    ###########################################################################
    collection5 = db["subscriptionData.provisionedData.amData"]
    # Json Data
    subsData_provision_am =   {
            "_id": ObjectId(),
            "gpsis": ["msisdn-"],
            "subscribedUeAmbr": {"uplink": "1 Gbps", "downlink": "2 Gbps"},
            "nssai": {
                "defaultSingleNssais": [ {"sst": 1.0, "sd": "010203"}, {"sst": 1.0, "sd": "112233"}  ]    },
            "ueId": UE_ID,
            "servingPlmnId": "20893"
        }
    # Insert the data into the collections
    res5 = collection5.insert_one(subsData_provision_am)
    # Print the inserted document's _id
    # print(res5.inserted_id)
    # Print the names of all databases on the MongoDB server
    # print("Database Names:", client.list_database_names())
    # Step 7: Reading the document that we insert. Retrieve a single document from the collection
    record5 = collection5.find_one()
    # Print the retrieved document
    print("subscriptionData.provisionedData.amData",record5)

    ###########################################################################
    collection6 = db["subscriptionData.provisionedData.smData"]
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
            "ueId": UE_ID,
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
            "ueId": UE_ID,
            "servingPlmnId": "20893"
        }
    ]
    # Insert the data into the collections
    res6 = collection6.insert_many(subsData_provision_sm)
    # Print the inserted document's _id
    # print(res6.inserted_ids)
    # Print the names of all databases on the MongoDB server
    # print("Database Names:", client.list_database_names())
    # Step 7: Reading the document that we insert. Retrieve a single document from the collection
    record6 = collection6.find_one()
    # Print the retrieved document
    print("subscriptionData.provisionedData.smData",record6)
    ###########################################################################
    collection7 = db["subscriptionData.provisionedData.smfSelectionSubscriptionData"]
    # Json Data
    subsData_provision_smf = {
            "_id": ObjectId(),
            "subscribedSnssaiInfos": {
                "01010203": {
                    "dnnInfos": [ {"dnn": "internet"}, {"dnn": "internet2"}
                    ]
                },
                "01112233": {
                    "dnnInfos": [ {"dnn": "internet"}, {"dnn": "internet2"}  ]  }
            },
            "ueId": UE_ID,
            "servingPlmnId": "20893"
        }

    # Insert the data into the collections
    res7 = collection7.insert_one(subsData_provision_smf)
    # Print the inserted document's _id
    print(res7.inserted_id)
    # Print the names of all databases on the MongoDB server
    print("Database Names:", client.list_database_names())
    # Step 7: Reading the document that we insert. Retrieve a single document from the collection
    record7 = collection7.find_one()
    # Print the retrieved document
    print(record7)

