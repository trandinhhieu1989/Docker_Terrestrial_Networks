# Check in Mongodb if UE's information is already exists, we need to update new information
# https://www.tutorialspoint.com/python_data_access/python_mongodb_update.htm#:~:text=You%20can%20update%20the%20contents,document%20with%20the%20new%20one.
# You can update the contents of an existing documents using the update() method or save() method.
# The update method modifies the existing document whereas the save method replaces the existing document with the new one.
from pymongo import MongoClient
import gridfs
from bson import ObjectId
from datetime import datetime

## Update UE's information into MongoDB
def Update_UE_function(UE_ID,permanentID,i):
    # Generate the current timestamp
    current_timestamp = datetime.now().isoformat()
    # Replace "mongodb://localhost:27017" with your MongoDB connection string
    client = MongoClient("mongodb://localhost:27017")

    # Access a specific database and collection
    db = client["free5gc"]

    # Insert a document into a collection polictyData_ues_amData.json referencing the file
    collection = db["policyData.ues.amData"]

    # Find i documents in collection
    cursor = collection.find({})

    # Iterate through the documents and retrieve the _id field
    ueids = [str(doc["ueId"]) for doc in cursor]
    # Print the list of ObjectId values
    print("All UE Ids",ueids)
    # Define the ObjectId of the document you want to update (replace with your actual ObjectId)
    target_ue_id = ueids[i-1]
    print("Target ue Id to update:", target_ue_id)
    filter = {"ueId": "target_ue_id"}  # Empty filter matches all documents
    # policyData.ues.smData
    new_values = {"subscCats": ["free5gc"], "ueId": UE_ID}
    # Update the data into the collections
    update = {"$set": new_values}
    res = collection.update_one(filter, update)
    # Print the updated document in collection
    if i==1:
        #  Print the updated document in collection
        print("policyData.ues.amData :", collection.find_one())
    elif i>=2:
        # Find all documents in the collection, skip the first two documents, and limit to one document
        cursor = collection.find().skip(i-1).limit(1)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("policyData.ues.amData :", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")

    ###########################################################################
    # Insert a document into a collection polictyData_ues_amData.json referencing the file
    collection1 = db["policyData.ues.smData"]
    # Find i documents in collection
    cursor = collection1.find({})
    # Iterate through the documents and retrieve the _id field
    ueids = [str(doc["ueId"]) for doc in cursor]
    # Print the list of ObjectId values
    print("All UE Ids", ueids)
    # Define the ObjectId of the document you want to update (replace with your actual ObjectId)
    target_ue_id = ueids[i - 1]
    print("Target ue Id to update:", target_ue_id)
    filter1 = {"ueId": "target_ue_id"}  # Empty filter matches all documents
    # policyData.ues.smData
    new_values1 = {
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
    # Update the data into the collections
    # collection1.replace_one({"_id": ObjectId()}, {'_id': ObjectId('f4f0f571ece402c810907f66')})
    update1 = {"$set": new_values1}
    res1 = collection1.update_one(filter1,update1 )
    # Print the updated document in collection
    if i == 1:
        #  Print the updated document in collection
        print("policyData.ues.smData :", collection.find_one())
    elif i >= 2:
        # Find all documents in the collection, skip the first two documents, and limit to one document
        cursor = collection1.find().skip(i - 1).limit(1)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("policyData.ues.smData:", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")
    ###########################################################################
    collection2 = db["subscriptionData.authenticationData.authenticationStatus"]
    # Find i documents in collection
    cursor = collection2.find({})
    # Iterate through the documents and retrieve the _id field
    ueids = [str(doc["ueId"]) for doc in cursor]
    # Print the list of ObjectId values
    print("All UE Ids", ueids)
    # Define the ObjectId of the document you want to update (replace with your actual ObjectId)
    target_ue_id = ueids[i - 1]
    print("Target ue Id to update:", target_ue_id)
    filter2 = {"ueId": "target_ue_id"}  # Empty filter matches all documents
    # Json Data
    new_values_2 = {  "nfInstanceId": "9ff8ef58-cdc2-4001-971f-d98dcb9ec81f",
            "success": True, "timeStamp": current_timestamp, "authType": "5G_AKA",
            "servingNetworkName": "5G:mnc093.mcc208.3gppnetwork.org",
            "ueId": UE_ID
        }
    # update the data into the collections
    # collection2.replace_one({"_id": ObjectId()}, {'_id': ObjectId('f4f0f571ece402c810907f67')})
    update2 = {"$set": new_values_2}
    res2 = collection2.update_one(filter2, update2)
    # Print the updated document in collection
    if i == 1:
        #  Print the updated document in collection
        print("subscriptionData.authenticationData.authenticationStatus:", collection.find_one())
    elif i >= 2:
        # Find all documents in the collection, skip the first i documents, and limit to one document
        cursor = collection2.find().skip(i - 1).limit(1)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("subscriptionData.authenticationData.authenticationStatus :", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")
    ###########################################################################
    #
    collection3 = db["subscriptionData.authenticationData.authenticationSubscription"]
    # Find i documents in collection
    cursor = collection3.find({})
    # Iterate through the documents and retrieve the _id field
    ueids = [str(doc["ueId"]) for doc in cursor]
    # Print the list of ObjectId values
    print("All UE Ids", ueids)
    # Define the ObjectId of the document you want to update (replace with your actual ObjectId)
    target_ue_id = ueids[i - 1]
    print("Target ue Id to update:", target_ue_id)
    filter3= {"ueId": "target_ue_id"}  # Empty filter matches all documents
    # Json Data
    new_values_3 = {
            "sequenceNumber": "000000000022","authenticationManagementField": "8000",
            "milenage": {  "op": { "encryptionAlgorithm": 0.0, "encryptionKey": 0.0, "opValue": "" }    },
            "opc": { "encryptionAlgorithm": 0.0, "encryptionKey": 0.0, "opcValue": "8e27b6af0e692e750f32667a3b14605d" },
            "ueId": UE_ID, "authenticationMethod": "5G_AKA",
            "permanentKey": {"permanentKeyValue": permanentID ,"encryptionAlgorithm": 0.0,"encryptionKey": 0.0 }
        }

    # update the data into the collections
    # collection3.replace_one({"_id": ObjectId()}, {'_id': ObjectId('f4f0f571ece402c810907f68')})
    update3 = {"$set": new_values_3}
    res3 = collection3.update_one(filter3, update3)
    # Print the updated document in collection
    if i == 1:
        #  Print the updated document in collection
        print("subscriptionData.authenticationData.authenticationSubscription :", collection.find_one())
    elif i >= 2:
        # Find all documents in the collection, skip the first two documents, and limit to one document
        cursor = collection3.find().skip(i - 1).limit(1)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("subscriptionData.authenticationData.authenticationSubscription :", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")
    ###########################################################################

    collection4 = db["subscriptionData.contextData.amf3gppAccess"]
    # Find i documents in collection
    cursor = collection4.find({})
    # Iterate through the documents and retrieve the _id field
    ueids = [str(doc["ueId"]) for doc in cursor]
    # Print the list of ObjectId values
    print("All UE Ids", ueids)
    # Define the ObjectId of the document you want to update (replace with your actual ObjectId)
    target_ue_id = ueids[i - 1]
    print("Target ue Id to update:", target_ue_id)
    filter4 = {"ueId": "target_ue_id"}  # Empty filter matches all documents
    # Json Data
    new_values_4 =  {
            "ratType": "", "ueId": UE_ID,
            "amfInstanceId": "d491a3cd-386c-45f3-ab2a-49c916f21b3d",
            "imsVoPs": "HOMOGENEOUS_NON_SUPPORT", "deregCallbackUri": "",
            "initialRegistrationInd": True,
            "guami": { "plmnId": {"mcc": "208", "mnc": "93"}, "amfId": "cafe00" }  }
    # Update the data into the collections
    # collection4.replace_one({"_id": ObjectId()}, {'_id': ObjectId('f4f0f571ece402c810907f69')})
    update4 = {"$set": new_values_4}
    res4 = collection4.update_one(filter4, update4)
    # Print the updated document in collection
    if i == 1:
        #  Print the updated document in collection
        print("subscriptionData.contextData.amf3gppAccess :", collection.find_one())
    elif i >= 2:
        # Find all documents in the collection, skip the first two documents, and limit to one document
        cursor = collection4.find().skip(i - 1).limit(1)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("subscriptionData.contextData.amf3gppAccess :", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")
    ###########################################################################
    collection5 = db["subscriptionData.provisionedData.amData"]
    # Find i documents in collection
    cursor = collection5.find({})
    # Iterate through the documents and retrieve the _id field
    ueids = [str(doc["ueId"]) for doc in cursor]
    # Print the list of ObjectId values
    print("All UE Ids", ueids)
    # Define the ObjectId of the document you want to update (replace with your actual ObjectId)
    target_ue_id = ueids[i - 1]
    print("Target ue Id to update:", target_ue_id)
    filter5 = {"ueId": "target_ue_id"}  # Empty filter matches all documents
    # Json Data
    new_values_5 =   { "gpsis": ["msisdn-"],
            "subscribedUeAmbr": {"uplink": "1 Gbps", "downlink": "2 Gbps"},
            "nssai": {
                "defaultSingleNssais": [ {"sst": 1.0, "sd": "010203"}, {"sst": 1.0, "sd": "112233"}  ]    },
            "ueId": UE_ID,
            "servingPlmnId": "20893"
        }
    # Update the data into the collections
    # collection5.replace_one({"_id": ObjectId()}, {'_id': ObjectId('f4f0f571ece402c810907f70')})
    update5 = {"$set": new_values_5}
    res5 = collection5.update_one(filter5, update5)
    # Print the updated document in collection
    if i == 1:
        #  Print the updated document in collection
        print("subscriptionData.provisionedData.amData :", collection.find_one())
    elif i >= 2:
        # Find all documents in the collection, skip the first two documents, and limit to one document
        cursor = collection5.find().skip(i - 1).limit(1)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("subscriptionData.provisionedData.amData :", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")

    ###########################################################################
    collection6 = db["subscriptionData.provisionedData.smData"]
    # Find i documents in collection
    cursor = collection6.find({})
    # Iterate through the documents and retrieve the _id field
    ueids = [str(doc["ueId"]) for doc in cursor]
    # Print the list of ObjectId values
    print("All UE Ids", ueids)
    # Define the ObjectId of the document you want to update (replace with your actual ObjectId)
    target_ue_id = ueids[2*i - 1]
    print("Target ue Id to update:", target_ue_id)
    filter6 = {"ueId": "target_ue_id"}  # Empty filter matches all documents
    # Json Data
    new_values_6 =   {
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
        }
    new_values_61 =   {
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

    # Update the data into the collections
    # collection6.replace_one({"_id": ObjectId()}, {'_id': ObjectId('f4f0f571ece402c810907f71')})
    update6 = {"$set": new_values_6}
    res6 = collection6.update_one(filter6, update6)
    update61 = {"$set": new_values_61}
    res61 = collection6.update_one(filter6, update61)
    # Print the updated document in collection
    if i == 1:
        # Find two first documents from the collections
        cursor = collection6.find().limit(2)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("subscriptionData.provisionedData.smData :", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")
    elif i >= 2:
        # Find all documents in the collection, skip the first two documents, and limit to one document
        cursor = collection6.find().skip(2*i - 2).limit(2)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("subscriptionData.provisionedData.smData :", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")
    ###########################################################################
    collection7 = db["subscriptionData.provisionedData.smfSelectionSubscriptionData"]
    # Find i documents in collection
    cursor = collection7.find({})
    # Iterate through the documents and retrieve the _id field
    ueids = [str(doc["ueId"]) for doc in cursor]
    # Print the list of ObjectId values
    print("All UE Ids", ueids)
    # Define the ObjectId of the document you want to update (replace with your actual ObjectId)
    target_ue_id = ueids[i - 1]
    print("Target ue Id to update:", target_ue_id)
    filter7 = {"ueId": "target_ue_id"}  # Empty filter matches all documents
    # Json Data
    new_values_7 = {
            "subscribedSnssaiInfos": {
                "01010203": {
                    "dnnInfos": [ {"dnn": "internet"}, {"dnn": "internet2"}
                    ]
                },
                "01112233": {
                    "dnnInfos": [ {"dnn": "internet"}, {"dnn": "internet2"}  ]  }
            },
            "servingPlmnId": "20893"
        }

    # Update the data into the collections
    # collection7.replace_one({"_id": ObjectId()}, {'_id': ObjectId('f4f0f571ece402c810907f73')})
    update7 = {"$set": new_values_7}
    res7 = collection7.update_one(filter7, update7 )
    # Print the updated document in collection
    if i == 1:
        #  Print the updated document in collection
        print("subscriptionData.provisionedData.smfSelectionSubscriptionData :", collection.find_one())
    elif i >= 2:
        # Find all documents in the collection, skip the first two documents, and limit to one document
        cursor = collection7.find().skip(i - 1).limit(1)
        # Initialize a count variable
        document_count = 0
        # Iterate through the cursor to count the documents
        for document in cursor:
            document_count += 1
            # Print the third document
            print("subscriptionData.provisionedData.smfSelectionSubscriptionData :", document)
        # Check if there were any documents in the cursor
        if document_count == 0:
            print("No updated document found")

