import streamlit as st
from firebase_admin import credentials, firestore, initialize_app

# Access Firebase secrets from Streamlit Cloud secrets
firebase_secrets = st.secrets["firebase"]

# Initialize Firebase Admin
cred = credentials.Certificate({
    "type": firebase_secrets["type"],
    "project_id": firebase_secrets["project_id"],
    "private_key_id": firebase_secrets["private_key_id"],
    "private_key": firebase_secrets["private_key"],
    "client_email": firebase_secrets["client_email"],
    "client_id": firebase_secrets["client_id"],
    "auth_uri": firebase_secrets["auth_uri"],
    "token_uri": firebase_secrets["token_uri"],
    "auth_provider_x509_cert_url": firebase_secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": firebase_secrets["client_x509_cert_url"]
})
initialize_app(cred)
db = firestore.client()

# Streamlit App
st.title("Firestore Data Viewer")

# Define your Firestore collection
collection_name = "dic_project"

# Fetch and display Firestore data
st.subheader("View Data from Firestore")
try:
    docs = db.collection(collection_name).stream()  # Fetch all documents
    data_list = [doc.to_dict() for doc in docs]  # Convert documents to a list of dictionaries

    if data_list:
        st.write("Data in Firestore:")
        st.write(data_list)  # Display all data as a list of dictionaries
    else:
        st.warning("No data found in the collection.")
except Exception as e:
    st.error(f"Error fetching data from Firestore: {e}")
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Before Firebase initialization
logging.debug("Initializing Firebase with secrets.")
logging.debug(f"Secrets: {firebase_secrets}")

