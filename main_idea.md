## Scanning the Books: 
This part will require a technique known as Optical Character Recognition (OCR) which is a field of research in pattern recognition, artificial intelligence and computer vision. Tools like Tesseract are useful here. Python has a library called pytesseract that can be used for this.

## Extracting Title and Author: 
After extracting the text from the images, you will need to implement Named Entity Recognition (NER) to identify and categorize the key information points from the text like the book's title and author. You can use libraries like spaCy or NLTK in Python for this.

## Storing as Numerical Database: 
The extracted information will need to be structured and stored. Python libraries like pandas can be used to create structured data formats like DataFrames, which can then be stored in a database using SQL libraries like sqlite3 or SQLAlchemy.

## Scanning the Resume: 
This will again involve OCR to convert images into text.

## Classifying by Resume: 
You will likely need to apply text classification techniques on the extracted text to classify the books based on their summaries. One way to do this would be to train a machine learning model to recognize different categories based on the book summaries. You could do this using libraries like scikit-learn, or if you want to use deep learning for this task, tensorflow or pytorch could be used. If your classification is based on predefined genres or topics, you could use topic modeling techniques (like Latent Dirichlet Allocation) to identify the main topics in each summary.

## Book Recommender: 
You mentioned in another comment about a book recommender system. If this is a part of the project, you can use techniques like Collaborative Filtering or Content-Based Filtering. You can implement these using the Python scikit-learn library or the surprise library, which is a Python scikit specifically for building and analyzing recommender systems.