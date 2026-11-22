# \# MongoDB Performance Assessment

# 

# \## Application Description

# 

# This Python application connects to a MongoDB database and allows users to manage Amazon product review data. The program uses an interactive menu to perform Create, Read, Update, and Delete (CRUD) operations.

# 

# \## Technologies Used

# 

# \- Python 3

# \- MongoDB

# \- MongoDB Compass

# \- PyMongo

# \- Python IDLE

# \- GitHub

# 

# \## Dependencies

# 

# The application requires Python, MongoDB, and the PyMongo library.

# 

# Install PyMongo using:

# 

# `pip install pymongo`

# 

# \## Database Information

# 

# \- \*\*Database:\*\* Amazon

# \- \*\*Collection:\*\* ReviewData

# \- \*\*Dataset:\*\* Amazon product reviews imported from a JSON file

# \- \*\*Connection:\*\* mongodb://localhost:27017/

# 

# \## Application Features

# 

# The application includes seven menu options:

# 

# 1\. \*\*Query for Documents:\*\* Search reviews by Review ID, star rating, words in the review title, or words in the review body.

# 2\. \*\*Add a New Document:\*\* Insert a new product review into the database.

# 3\. \*\*Update Fields of a Document:\*\* Modify an existing review using its Review ID.

# 4\. \*\*Delete a Document:\*\* Remove a specific review using its Review ID.

# 5\. \*\*Delete All Documents:\*\* Remove all documents from the ReviewData collection.

# 6\. \*\*Delete a Collection:\*\* Remove the ReviewData collection from the database.

# 7\. \*\*Exit the Program:\*\* Close the application.

# 

# \## How to Run the Application

# 

# 1\. Install Python and MongoDB.

# 2\. Install the PyMongo library.

# 3\. Start the local MongoDB server.

# 4\. Open MongoDB Compass and connect to `mongodb://localhost:27017/`.

# 5\. Create the Amazon database and ReviewData collection if they do not already exist.

# 6\. Import the Amazon review JSON dataset into ReviewData.

# 7\. Open `MongoDB\_PA.py` in Python IDLE.

# 8\. Select \*\*Run → Run Module\*\* or press F5.

# 9\. Follow the menu prompts to perform database operations.

# 

# \## Testing

# 

# The application was tested using 5,000 Amazon review documents. All seven menu options were tested successfully, including querying, inserting, updating, deleting documents, removing the collection, and exiting the program.

# 

# \## Author

# 

# Lastazia Dickens

# 

# ECPI University — MongoDB Performance Assessment

