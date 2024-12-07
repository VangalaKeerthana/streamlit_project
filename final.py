import streamlit as st
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase Admin
cred = credentials.Certificate("C:/Users/vanga/Downloads/dic_1/key.json")  # Update with your key file path
initialize_app(cred)
db = firestore.client()

# Streamlit App
st.title("Firestore Data Viewer")

# Define your Firestore collection
collection_name = "dic_project"  # Replace with your collection name

# Fetch and display Firestore data
st.subheader("View Data from Firestore")
try:
    docs = db.collection(collection_name).stream()  # Fetch all documents from the collection
    data_list = [doc.to_dict() for doc in docs]  # Convert documents to a list of dictionaries

    if data_list:
        st.write("Data in Firestore:")
        st.write(data_list)  # Display all data as a list of dictionaries
    else:
        st.warning("No data found in the collection.")
except Exception as e:
    st.error(f"Error fetching data from Firestore: {e}")
