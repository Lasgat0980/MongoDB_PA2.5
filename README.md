
# MongoDB Performance Assessment

## Application Description
This Python application connects to MongoDB to manage Amazon product reviews using Create, Read, Update, and Delete (CRUD) operations.

## Technologies and Requirements
- Python 3
- MongoDB
- MongoDB Compass
- PyMongo
- Python IDLE

## Installation
Install PyMongo using:

`pip install pymongo`

## Database Information
- Database: Amazon
- Collection: ReviewData
- Dataset: Amazon product reviews (JSON)
- Connection: mongodb://localhost:27017/

## Application Features
1. Query documents by Review ID, stars, title, or review body.
2. Add a new document.
3. Update an existing document.
4. Delete a specific document.
5. Delete all documents from the collection.
6. Delete the collection.
7. Exit the program.

## How to Run
1. Install Python, MongoDB, and PyMongo.
2. Start MongoDB.
3. Connect through MongoDB Compass.
4. Create the Amazon database and ReviewData collection.
5. Import the Amazon review JSON dataset.
6. Open MongoDB_PA.py in Python IDLE.
7. Press F5 to run the application.
8. Select an option from the menu.

## Testing
The application was tested using 5,000 Amazon review documents. All seven menu options were tested successfully.

## Author
Lastazia Dickens  
ECPI University
