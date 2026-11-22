# Name: Lastazia Dickens

# Name: Lastazia Dickens
# Date: November 22, 2026
# Assignment: 2.5 Performance Assessment: Python Application Accessing a Document Database
# Objective: Create a Python application that allows users to
# perform CRUD operations on a MongoDB document database.

import json
import pymongo

# *** CREATE SECTION***
#Notify when script is starting
print("Connecting to local Mongo database...")

#Connect to the local Mongo database
myClient = pymongo.MongoClient("mongodb://localhost:27017/")

#Create a new database
db = myClient["Amazon"]

#Create a new collection in the database
myCollection = db["ReviewData"]

#Display status of database
print("List of available databases: ")
print(myClient.list_database_names())
print("List of available collections in this database: ")
print(db.list_collection_names())

while True:
    print("\nType in a number and press enter to execute the menu option.")
    print("1. Query for documents")
    print("2. Add a new document")
    print("3. Update fields of a document")
    print("4. Delete a document")
    print("5. Delete all documents from the collection")
    print("6. Delete a collection")
    print("7. Exit the program")

    choice = input()

    # *** READ SECTION ***
    #Display a document
    if choice == "1":
        print("\nPlease type in a number and press enter to execute the menu option")
        print("1. Query by reviewID")
        print("2. Filter for a number of stars and greater")
        print("3. Filter for less than a number of stars")
        print("4. Filter for a word in the title")
        print("5. Filter for a word in the review body content")

        queryChoice = input()

        if queryChoice == "1":
            reviewID = input("Enter the ReviewID: ")
            sampleData = myCollection.find_one({"review_id": reviewID})
            print(sampleData)

        #Filter for only 4 and 5 star reviews and limit to 3 results
        elif queryChoice == "2":
            stars = input("Enter the number of stars: ")
            query = {"stars": {"$gte": stars}}
            showFields = {"_id": False, "review_body": True, "stars": True}
            data = myCollection.find(query, showFields).limit(3)

            for doc in data:
                print(doc)
                print()

        elif queryChoice == "3":
            stars = input("Enter the number of stars: ")
            query = {"stars": {"$lt": stars}}
            showFields = {"_id": False, "review_body": True, "stars": True}
            data = myCollection.find(query, showFields).limit(3)

            for doc in data:
                print(doc)
                print()

        #Filter for a word in the review_title, limit results
        elif queryChoice == "4":
            word = input("Search the title for:\n")
            query = {"review_title": {"$regex": word, "$options": "i"}}
            showFields = {"_id": False, "review_title": True, "review_body": True}
            data = myCollection.find(query, showFields).limit(3)

            for doc in data:
                print(doc)
                print()

        elif queryChoice == "5":
            word = input("Search the review body for:\n")
            query = {"review_body": {"$regex": word, "$options": "i"}}
            showFields = {"_id": False, "review_title": True, "review_body": True}
            data = myCollection.find(query, showFields).limit(3)

            for doc in data:
                print(doc)
                print()

    # *** CREATE SECTION***
    #Insert a new document into the collection
    elif choice == "2":
        print("\nEnter the information for the new document.")

        reviewID = input("Review ID: ")
        productID = input("Product ID: ")
        reviewerID = input("Reviewer ID: ")
        stars = input("Stars: ")
        reviewBody = input("Review Body: ")
        reviewTitle = input("Review Title: ")
        language = input("Language: ")
        productCategory = input("Product Category: ")

        newData = {
            "review_id": reviewID,
            "product_id": productID,
            "reviewer_id": reviewerID,
            "stars": stars,
            "review_body": reviewBody,
            "review_title": reviewTitle,
            "language": language,
            "product_category": productCategory
        }

        insertQuery = myCollection.insert_one(newData)
        print("New document inserted.")

    # *** UPDATE SECTION ***
    #Update a document in the collection
    elif choice == "3":
        reviewID = input("\nWhat is the ReviewID you wish to update?\n")
        field = input("Which field would you like to update?\n")
        value = input("What would you like to change the value to?\n")

        fields = [
            "review_id", "product_id", "reviewer_id", "stars",
            "review_body", "review_title", "language",
            "product_category"
        ]

        if field in fields:
            query = {"review_id": reviewID}
            updateData = {"$set": {field: value}}
            result = myCollection.update_one(query, updateData)

            if result.matched_count > 0:
                print("New document has been updated to: ")
                print(myCollection.find_one({"review_id": reviewID}))
            else:
                print("Document not found.")
        else:
            print("Invalid field name.")

    # *** DELETE SECTION ***
    #Delete a single document from the collection
    elif choice == "4":
        reviewID = input(
            "\nWhat is the ReviewID of the document you wish to delete?\n"
        )

        query = {"review_id": reviewID}
        result = myCollection.delete_one(query)

        if result.deleted_count > 0:
            print("Document deleted!")
        else:
            print("Document not found.")

    #Delete all documents from the collection
    elif choice == "5":
        print("\nRemoving all documents from the collection...")
        removeData = myCollection.delete_many({})

        print("Number of documents deleted: " +
              str(removeData.deleted_count))

    #Delete a collection
    elif choice == "6":
        myCollection.drop()
        print("Collection removed!")

    #Display end of program message
    elif choice == "7":
        print("Program has ended!")
        break

    else:
        print("Invalid menu option. Please try again.")

