#!/media/hieutran/f4f77ea7-e872-d901-70e2-7ea7e872d901/Dockerfree5gc_github/myenv/bin/python3

from pymongo import MongoClient
import gridfs
from bson import ObjectId

# MongoDB connection parameters
# mongo_host = "172.18.0.2"  # 172.18.0.2 Use the container's IP or hostname if not running on localhost
# mongo_port = 27017
# mongo_username = "admin"
# mongo_password = "adminpass"
# auth_db = "admin"
#
# # Create a MongoDB client
# client = MongoClient(
#     f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/{auth_db}"
# )

# Replace "mongodb://localhost:27017" with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017")

# Access a specific database and collection
db = client["free5gc"]

# # Example: Insert a document
# data = {"name": "John", "age": 30}
# collection.insert_one(data)
# print("Document inserted successfully")

# Create a new GridFS instance
# fs = gridfs.GridFS(db)
# file_path = "/media/hieu/E/Hieu/Dockerfree5gc_github/Pymongo/config.yaml"
# with open(file_path, "rb") as file:
#     file_contents = file.read()

# Insert the file into GridFS, You use the fs.put() method to insert the file contents into the GridFS. This returns a unique file ID.
# file_id = fs.put(file_contents, filename="UE_info_config_file.txt")

# Insert a document into a collection polictyData_ues_amData.json referencing the file
collection = db["policyData.ues.amData"]

# polictyData_ues_amData.json data to be inserted into the collections
Policy_data_am = {
    "_id":  ObjectId(),
    "subscCats": ["free5gc"],
    "ueId": "imsi-208930000000003"
}
# Insert the data into the collections
res = collection.insert_one(Policy_data_am)
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record = collection.find_one()
# Print the retrieved document
print(record)
###########################################################################
# Insert a document into a collection polictyData_ues_amData.json referencing the file
collection1 = db["policyData.ues.smData"]
# policyData.ues.smData
Policy_data_sm = {
    "_id":  ObjectId(),
    "smPolicySnssaiData": {
        "01010203": {
            "snssai": {
                "sst": 1.0,
                "sd": "010203"
            },
            "smPolicyDnnData": {
                "internet": {
                    "dnn": "internet"
                },
                "internet2": {
                    "dnn": "internet2"
                }
            }
        },
        "01112233": {
            "snssai": {
                "sst": 1.0,
                "sd": "112233"
            },
            "smPolicyDnnData": {
                "internet": {
                    "dnn": "internet"
                },
                "internet2": {
                    "dnn": "internet2"
                }
            }
        }
    },
    "ueId": "imsi-208930000000003"
}
# Insert the data into the collections
res1 = collection1.insert_one(Policy_data_sm)

# Print the inserted document's _id
print(res1.inserted_id)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record1 = collection1.find_one()
# Print the retrieved document
print(record1)
###########################################################################
#
collection2 = db["subscriptionData.authenticationData.authenticationSubscription"]
# Json Data
subsData_auth = {
    "_id": ObjectId(),
    "permanentKey": {
        "permanentKeyValue": "8baf473f2f8fd09487cccbd7097c6862",
        "encryptionKey": 0.0,
        "encryptionAlgorithm": 0.0
    },
    "sequenceNumber": "16f3b3f70fc2",
    "authenticationManagementField": "8000",
    "milenage": {
        "op": {
            "opValue": "",
            "encryptionKey": 0.0,
            "encryptionAlgorithm": 0.0
        }
    },
    "opc": {
        "opcValue": "8e27b6af0e692e750f32667a3b14605d",
        "encryptionKey": 0.0,
        "encryptionAlgorithm": 0.0
    },
    "ueId": "imsi-208930000000003",
    "authenticationMethod": "5G_AKA"
}
# Insert the data into the collections
res2 = collection2.insert_one(subsData_auth)

# Print the inserted document's _id
print(res2.inserted_id)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record2 = collection2.find_one()
# Print the retrieved document
print(record2)
###########################################################################
collection3 = db["subscriptionData.provisionedData.amData"]
# Json Data
subsData_provision_am = {
    "_id": ObjectId(),
    "nssai": {
        "defaultSingleNssais": [
            {"sd": "010203", "sst": 1.0},
            {"sd": "112233", "sst": 1.0}
        ]
    },
    "ueId": "imsi-208930000000003",
    "servingPlmnId": "20893",
    "gpsis": ["msisdn-"],
    "subscribedUeAmbr": {
        "downlink": "2 Gbps",
        "uplink": "1 Gbps"
    }
}
# Insert the data into the collections
res3 = collection3.insert_one(subsData_provision_am)

# Print the inserted document's _id
print(res3.inserted_id)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record3 = collection3.find_one()
# Print the retrieved document
print(record3)

###########################################################################
collection4 = db["subscriptionData.provisionedData.smData"]
# Json Data
subsData_provision_sm1 = {
    "_id": ObjectId(),
    "dnnConfigurations": {
        "internet": {
            "pduSessionTypes": {"allowedSessionTypes": ["IPV4"], "defaultSessionType": "IPV4"},
            "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
            "5gQosProfile": {"priorityLevel": 8.0, "5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}},
            "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"}
        },
        "internet2": {
            "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
            "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
            "5gQosProfile": {"5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}, "priorityLevel": 8.0},
            "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"}
        }
    },
    "ueId": "imsi-208930000000003",
    "servingPlmnId": "20893",
    "singleNssai": {"sst": 1.0, "sd": "010203"}
}

subsData_provision_sm2 = {
    "_id": ObjectId(),
    "dnnConfigurations": {
        "internet": {
            "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
            "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]},
            "5gQosProfile": {"5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}, "priorityLevel": 8.0},
            "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"}
        },
        "internet2": {
            "5gQosProfile": {"5qi": 9.0, "arp": {"priorityLevel": 8.0, "preemptCap": "", "preemptVuln": ""}, "priorityLevel": 8.0},
            "sessionAmbr": {"uplink": "200 Mbps", "downlink": "100 Mbps"},
            "pduSessionTypes": {"defaultSessionType": "IPV4", "allowedSessionTypes": ["IPV4"]},
            "sscModes": {"defaultSscMode": "SSC_MODE_1", "allowedSscModes": ["SSC_MODE_2", "SSC_MODE_3"]}
        }
    },
    "ueId": "imsi-208930000000003",
    "servingPlmnId": "20893",
    "singleNssai": {"sst": 1.0, "sd": "112233"}
}
# Insert the data into the collections
res4 = collection4.insert_many([subsData_provision_sm1, subsData_provision_sm2])
# Print the inserted document's _id
print(res4.inserted_ids)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record4 = collection4.find_one()
# Print the retrieved document
print(record4)
###########################################################################
collection5 = db["subscriptionData.provisionedData.smfSelectionSubscriptionData"]
# Json Data
subsData_provision_smf = {
    "_id": ObjectId(),
    "ueId": "imsi-208930000000003",
    "servingPlmnId": "20893",
    "subscribedSnssaiInfos": {
        "01010203": {
            "dnnInfos": [{"dnn": "internet"}, {"dnn": "internet2"}]
        },
        "01112233": {
            "dnnInfos": [{"dnn": "internet"}, {"dnn": "internet2"}]
        }
    }
}

# Insert the data into the collections
res5 = collection5.insert_one(subsData_provision_smf)
# Print the inserted document's _id
print(res5.inserted_id)
# Print the names of all databases on the MongoDB server
print("Database Names:", client.list_database_names())
# Step 7: Reading the document that we insert. Retrieve a single document from the collection
record5 = collection5.find_one()
# Print the retrieved document
print(record5)
###########################################################################
# collection6 = db["NfProfile"]
# # Json Data
# NfProfile1 = {
#     "_id": ObjectId(),
#     "nfInstanceId": "4610c783-ccc9-46db-bc04-7f801cf6dd51",
#     "nfType": "AMF",
#     "nfStatus": "REGISTERED",
#     "plmnList": [{"mcc": "208", "mnc": "93"}],
#     "sNssais": [{"sst": 1.0, "sd": "010203"}, {"sst": 1.0, "sd": "112233"}],
#     "ipv4Addresses": ["172.18.0.4"],
#     "amfInfo": {
#         "amfSetId": "3f8",
#         "amfRegionId": "ca",
#         "guamiList": [{"plmnId": {"mnc": "93", "mcc": "208"}, "amfId": "cafe00"}],
#         "taiList": [{"plmnId": {"mcc": "208", "mnc": "93"}, "tac": "000001"}]
#     },
#     "nfServices": [
#         {
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.4", "transport": "TCP", "port": 8000.0}],
#             "apiPrefix": "http://172.18.0.4:8000",
#             "serviceInstanceId": "0",
#             "serviceName": "namf-comm",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.9"}],
#             "scheme": "http"
#         },
#         {
#             "apiPrefix": "http://172.18.0.4:8000",
#             "serviceInstanceId": "1",
#             "serviceName": "namf-evts",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.9"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.4", "transport": "TCP", "port": 8000.0}]
#         },
#         {
#             "serviceName": "namf-mt",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.9"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.4", "transport": "TCP", "port": 8000.0}],
#             "apiPrefix": "http://172.18.0.4:8000",
#             "serviceInstanceId": "2"
#         },
#         {
#             "serviceInstanceId": "3",
#             "serviceName": "namf-loc",
#             "versions": [{"apiFullVersion": "1.0.9", "apiVersionInUri": "v1"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"transport": "TCP", "port": 8000.0, "ipv4Address": "172.18.0.4"}],
#             "apiPrefix": "http://172.18.0.4:8000"
#         },
#         {
#             "serviceInstanceId": "4",
#             "serviceName": "namf-oam",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.9"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.4", "transport": "TCP", "port": 8000.0}],
#             "apiPrefix": "http://172.18.0.4:8000"
#         }
#     ]
# }
#
# NfProfile2 = {
#     "_id": ObjectId(),
#     "nfInstanceId": "a12ad9f0-981d-43fa-acce-a51c1d2a8244",
#     "smfInfo": {
#         "sNssaiSmfInfoList": [
#             {"sNssai": {"sst": 1.0, "sd": "010203"}, "dnnSmfInfoList": [{"dnn": "internet"}]},
#             {"sNssai": {"sst": 1.0, "sd": "112233"}, "dnnSmfInfoList": [{"dnn": "internet"}]}
#         ]
#     },
#     "nfType": "SMF",
#     "nfStatus": "REGISTERED",
#     "plmnList": [{"mnc": "93", "mcc": "208"}],
#     "sNssais": [{"sst": 1.0, "sd": "010203"}, {"sst": 1.0, "sd": "112233"}],
#     "ipv4Addresses": ["172.18.0.6"],
#     "locality": "area1",
#     "nfServices": [
#         {
#             "serviceInstanceId": "a12ad9f0-981d-43fa-acce-a51c1d2a8244nsmf-pdusession",
#             "serviceName": "nsmf-pdusession",
#             "versions": [
#                 {
#                     "apiVersionInUri": "v1",
#                     "apiFullVersion": "https://172.18.0.6:8000/nsmf-pdusession/v1",
#                     "expiry": "2023-08-18T21:10:40.964581561Z"
#                 }
#             ],
#             "scheme": "https",
#             "nfServiceStatus": "REGISTERED",
#             "apiPrefix": "http://172.18.0.6:8000"
#         },
#         {
#             "nfServiceStatus": "REGISTERED",
#             "apiPrefix": "http://172.18.0.6:8000",
#             "serviceInstanceId": "a12ad9f0-981d-43fa-acce-a51c1d2a8244nsmf-event-exposure",
#             "serviceName": "nsmf-event-exposure",
#             "versions": [
#                 {
#                     "expiry": "2023-08-18T21:10:40.964581561Z",
#                     "apiVersionInUri": "v1",
#                     "apiFullVersion": "https://172.18.0.6:8000/nsmf-pdusession/v1"
#                 }
#             ],
#             "scheme": "https"
#         },
#         {
#             "serviceInstanceId": "a12ad9f0-981d-43fa-acce-a51c1d2a8244nsmf-oam",
#             "serviceName": "nsmf-oam",
#             "versions": [
#                 {
#                     "apiVersionInUri": "v1",
#                     "apiFullVersion": "https://172.18.0.6:8000/nsmf-pdusession/v1",
#                     "expiry": "2023-08-18T21:10:40.964581561Z"
#                 }
#             ],
#             "scheme": "https",
#             "nfServiceStatus": "REGISTERED",
#             "apiPrefix": "http://172.18.0.6:8000"
#         }
#     ]
# }
#
# NfProfile3 = {
#     "_id": ObjectId(),
#     "nfStatus": "REGISTERED",
#     "plmnList": [{"mcc": "208", "mnc": "93"}, {"mcc": "123", "mnc": "45"}],
#     "ipv4Addresses": ["172.18.0.7"],
#     "ausfInfo": {"groupId": "ausfGroup001"},
#     "nfServices": [
#         {
#             "serviceInstanceId": "a65489c3-851c-463d-bfec-52e580e101e0",
#             "serviceName": "nausf-auth",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.3"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"port": 8000.0, "ipv4Address": "172.18.0.7"}]
#         }
#     ],
#     "nfInstanceId": "a65489c3-851c-463d-bfec-52e580e101e0",
#     "nfType": "AUSF"
# }
#
# NfProfile4 = {
#     "_id": ObjectId(),
#     "nfServices": [
#         {
#             "serviceInstanceId": "0",
#             "serviceName": "nnssf-nsselection",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.8", "transport": "TCP", "port": 8000.0}],
#             "apiPrefix": "http://172.18.0.8:8000"
#         },
#         {
#             "serviceInstanceId": "1",
#             "serviceName": "nnssf-nssaiavailability",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.8", "transport": "TCP", "port": 8000.0}],
#             "apiPrefix": "http://172.18.0.8:8000"
#         }
#     ],
#     "nfInstanceId": "2a881a2b-c362-4dff-9067-fd275d810d1d",
#     "nfType": "NSSF",
#     "nfStatus": "REGISTERED",
#     "plmnList": [{"mcc": "208", "mnc": "93"}],
#     "ipv4Addresses": ["172.18.0.8"]
# }
#
# NfProfile5 = {
#     "_id": ObjectId(),
#     "nfType": "PCF",
#     "nfStatus": "REGISTERED",
#     "plmnList": [{"mcc": "208", "mnc": "93"}],
#     "ipv4Addresses": ["172.18.0.9"],
#     "locality": "area1",
#     "pcfInfo": {"dnnList": ["free5gc", "internet"]},
#     "nfServices": [
#         {
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"port": 8000.0, "ipv4Address": "172.18.0.9", "transport": "TCP"}],
#             "apiPrefix": "http://172.18.0.9:8000",
#             "serviceInstanceId": "0",
#             "serviceName": "npcf-am-policy-control"
#         },
#         {
#             "apiPrefix": "http://172.18.0.9:8000",
#             "supportedFeatures": "3fff",
#             "serviceInstanceId": "1",
#             "serviceName": "npcf-smpolicycontrol",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"port": 8000.0, "ipv4Address": "172.18.0.9", "transport": "TCP"}]
#         },
#         {
#         "ipEndPoints": [{"ipv4Address": "172.18.0.9", "transport": "TCP", "port": 8000.0}],
#         "apiPrefix": "http://172.18.0.9:8000",
#         "serviceInstanceId": "2",
#         "serviceName": "npcf-bdtpolicycontrol",
#         "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}],
#         "scheme": "http",
#         "nfServiceStatus": "REGISTERED"
#         },
#         {
#         "nfServiceStatus": "REGISTERED",
#         "ipEndPoints": [{"ipv4Address": "172.18.0.9", "transport": "TCP", "port": 8000.0}],
#         "apiPrefix": "http://172.18.0.9:8000",
#         "supportedFeatures": "3",
#         "serviceInstanceId": "3",
#         "serviceName": "npcf-policyauthorization",
#         "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}],
#         "scheme": "http"
#         },
#         {
#         "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}],
#         "scheme": "http",
#         "nfServiceStatus": "REGISTERED",
#         "ipEndPoints": [{"transport": "TCP", "port": 8000.0, "ipv4Address": "172.18.0.9"}],
#         "apiPrefix": "http://172.18.0.9:8000",
#         "serviceInstanceId": "4",
#         "serviceName": "npcf-eventexposure"
#         },
#         {
#         "serviceInstanceId": "5",
#         "serviceName": "npcf-ue-policy-control",
#         "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}],
#         "scheme": "http",
#         "nfServiceStatus": "REGISTERED",
#         "ipEndPoints": [{"ipv4Address": "172.18.0.9", "transport": "TCP", "port": 8000.0}],
#         "apiPrefix": "http://172.18.0.9:8000"
#         }
#     ],
#     "nfInstanceId": "f087d9cb-13a1-4af5-8b34-180661497acd"
# }
# NfProfile6 = {
#     "_id": ObjectId(),
#     "nfServices": [
#         {
#             "apiPrefix": "http://172.18.0.10:8000",
#             "serviceInstanceId": "0",
#             "serviceName": "nudm-sdm",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.3"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"transport": "TCP", "port": 8000.0, "ipv4Address": "172.18.0.10"}]
#         },
#         {
#             "serviceInstanceId": "1",
#             "serviceName": "nudm-uecm",
#             "versions": [{"apiFullVersion": "1.0.3", "apiVersionInUri": "v1"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.10", "transport": "TCP", "port": 8000.0}],
#             "apiPrefix": "http://172.18.0.10:8000"
#         },
#         {
#             "serviceInstanceId": "2",
#             "serviceName": "nudm-ueau",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.3"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"port": 8000.0, "ipv4Address": "172.18.0.10", "transport": "TCP"}],
#             "apiPrefix": "http://172.18.0.10:8000"
#         },
#         {
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.10", "transport": "TCP", "port": 8000.0}],
#             "apiPrefix": "http://172.18.0.10:8000",
#             "serviceInstanceId": "3",
#             "serviceName": "nudm-ee",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.3"}]
#         },
#         {
#             "ipEndPoints": [{"transport": "TCP", "port": 8000.0, "ipv4Address": "172.18.0.10"}],
#             "apiPrefix": "http://172.18.0.10:8000",
#             "serviceInstanceId": "4",
#             "serviceName": "nudm-pp",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.3"}],
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED"
#         }
#     ],
#     "nfInstanceId": "c0326e74-2075-4ff8-b79d-f5e721ffcde1",
#     "nfType": "UDM",
#     "nfStatus": "REGISTERED",
#     "plmnList": [{"mcc": "208", "mnc": "93"}],
#     "ipv4Addresses": ["172.18.0.10"],
#     "udmInfo": {}
# }
#
# NfProfile7 = {
#     "_id": ObjectId(),
#     "nfType": "UDR",
#     "nfStatus": "REGISTERED",
#     "plmnList": [{"mcc": "208", "mnc": "93"}],
#     "ipv4Addresses": ["172.18.0.11"],
#     "udrInfo": {"supportedDataSets": ["SUBSCRIPTION"]},
#     "nfServices": [
#         {
#             "scheme": "http",
#             "nfServiceStatus": "REGISTERED",
#             "ipEndPoints": [{"ipv4Address": "172.18.0.11", "transport": "TCP", "port": 8000.0}],
#             "apiPrefix": "http://172.18.0.11:8000",
#             "serviceInstanceId": "datarepository",
#             "serviceName": "nudr-dr",
#             "versions": [{"apiVersionInUri": "v1", "apiFullVersion": "1.0.2"}]
#         }
#     ],
#     "nfInstanceId": "efd95e95-7556-4a6d-8dfa-36cc3eece33b"
# }
#
# # Insert the data into the collections
# res6 = collection6.insert_many([NfProfile1, NfProfile2,NfProfile3, NfProfile4,NfProfile5,NfProfile6,NfProfile7])
# # Print the inserted document's _id
# print(res6.inserted_ids)
# # Print the names of all databases on the MongoDB server
# print("Database Names:", client.list_database_names())
# # Step 7: Reading the document that we insert. Retrieve a single document from the collection
# record6 = collection6.find_one()
# # Print the retrieved document
# print(record6)

#################################################################################
# collection7 = db["urilist"]
# # Json Data
# urilist = [
#     {
#         "_id": ObjectId(),
#         "nfType": "AMF",
#         "_link": {"item": [{"href": "http://172.18.0.3:8000/nnrf-nfm/v1/nf-instances/4610c783-ccc9-46db-bc04-7f801cf6dd51"}]}
#     },
#     {
#         "_id": ObjectId(),
#         "nfType": "SMF",
#         "_link": {"item": [{"href": "http://172.18.0.3:8000/nnrf-nfm/v1/nf-instances/a12ad9f0-981d-43fa-acce-a51c1d2a8244"}]}
#     },
#     {
#         "_id": ObjectId(),
#         "nfType": "AUSF",
#         "_link": {"item": [{"href": "http://172.18.0.3:8000/nnrf-nfm/v1/nf-instances/a65489c3-851c-463d-bfec-52e580e101e0"}]}
#     },
#     {
#         "_id": ObjectId(),
#         "nfType": "NSSF",
#         "_link": {"item": [{"href": "http://172.18.0.3:8000/nnrf-nfm/v1/nf-instances/2a881a2b-c362-4dff-9067-fd275d810d1d"}]}
#     },
#     {
#         "_id": ObjectId(),
#         "nfType": "PCF",
#         "_link": {"item": [{"href": "http://172.18.0.3:8000/nnrf-nfm/v1/nf-instances/f087d9cb-13a1-4af5-8b34-180661497acd"}]}
#     },
#     {
#         "_id": ObjectId(),
#         "nfType": "UDM",
#         "_link": {"item": [{"href": "http://172.18.0.3:8000/nnrf-nfm/v1/nf-instances/c0326e74-2075-4ff8-b79d-f5e721ffcde1"}]}
#     },
#     {
#         "_id": ObjectId(),
#         "nfType": "UDR",
#         "_link": {"item": [{"href": "http://172.18.0.3:8000/nnrf-nfm/v1/nf-instances/efd95e95-7556-4a6d-8dfa-36cc3eece33b"}]}
#     }
# ]
#
#
# # Insert the data into the collections
# res7 = collection7.insert_many(urilist)
# # Print the inserted document's _id
# print(res7.inserted_ids)
# # Print the names of all databases on the MongoDB server
# print("Database Names:", client.list_database_names())
# # Step 7: Reading the document that we insert. Retrieve a single document from the collection
# record7 = collection6.find_one()
# # Print the retrieved document
# print(record7)



#################################################################################
'''# Step 8: Update the record that we have inserted
query = {
    "message": "This is pymongo demo"
}
new_val = {
    "$set":{"message": "welcome to coding with me"}
}
new_record = collection.update_one(query, new_val)
print(new_record)
#Reading the document after updating
record = collection.find_one()
print(record)'''

print("we already insert config dot yaml file into MongoDB")
# Close the MongoDB connection
client.close()
