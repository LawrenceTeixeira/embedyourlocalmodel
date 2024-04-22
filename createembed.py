# Importing necessary libraries and modules
import os
import pyodbc  # SQL connection library for Microsoft databases
import requests  # For making HTTP requests
from dotenv import load_dotenv  # To load environment variables from a .env file
import numpy as np  # Library for numerical operations
from sklearn.preprocessing import normalize  # For normalizing data
import json  # For handling JSON data
from db.utils import NpEncoder  # Custom JSON encoder for numpy data types

# Load environment variables from a .env file located in the same directory
load_dotenv()

# This is the connection string for connecting to the Azure SQL database we are getting from the environment variables
#MSSQL='Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=<DATABASE NAME>;Uid=<USER>;Pwd=<PASSWOPRD>;Encrypt=No;Connection Timeout=30;'

# Retrieve the database connection string from environment variables
dbconnectstring = os.getenv('MSSQL')

# Establish a connection to the Azure SQL database using the connection string
conn = pyodbc.connect(dbconnectstring)

def get_embedding(text, model):
    # Prepare the input text by truncating it or preprocessing if needed
    truncated_text = text

    # Make an HTTP POST request to a local server API to get embeddings for the input text
    res = requests.post(url='http://localhost:11434/api/embeddings',
                        json={
                            'model': model, 
                            'prompt': truncated_text
                        }
    )
    
    # Extract the embedding from the JSON response
    embeddings = res.json()['embedding']
    
    # Convert the embedding list to a numpy array
    embeddings = np.array(embeddings)    
    
    # Normalize the embeddings array to unit length
    nc = normalize([embeddings])
        
    # Convert the numpy array back to JSON string using a custom encoder that handles numpy types
    return json.dumps(nc[0], cls=NpEncoder )

def update_database(id, title_vector, content_vector):
    # Obtain a new cursor from the database connection
    cursor = conn.cursor()

    # Convert numpy array embeddings to string representations for storing in SQL
    title_vector_str = str(title_vector)
    content_vector_str = str(content_vector)

    # SQL query to update the embeddings in the database
    cursor.execute("""
        UPDATE wikipedia_articles_embeddings
        SET title_vector = ?, content_vector = ?
        WHERE id = ?
    """, (title_vector_str, content_vector_str, id))
    conn.commit()  # Commit the transaction to the database

def embed_and_update(model):
    # Get a cursor from the database connection
    cursor = conn.cursor()
    
    # Retrieve articles from the database that need their embeddings updated
    cursor.execute("select id, title, text from wikipedia_articles_embeddings where title_vector = '' or content_vector = '' order by id desc")
    
    for row in cursor.fetchall():
        id, title, text = row
        
        # Get embeddings for title and text
        title_vector = get_embedding(title, model)
        content_vector = get_embedding(text, model)
        
        # Print the progress with length of the generated embeddings
        print(f"Embedding article {id} - {title}", "len:", len(title_vector), len(content_vector))
        
        # Update the database with new embeddings
        update_database(id, title_vector, content_vector)

# Call the function to update embeddings using the 'nomic-embed-text' model
embed_and_update('nomic-embed-text')

# To use another model, uncomment and call the function with the different model name
# embed_and_update('mxbai-embed-large')
