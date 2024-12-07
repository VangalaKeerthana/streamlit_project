import streamlit as st
from firebase_admin import credentials, firestore, initialize_app
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Access Firebase secrets from Streamlit Cloud secrets
firebase_secrets = st.secrets["firebase"]

# Log initialization step (excluding sensitive data)
logging.debug("Initializing Firebase Admin with provided secrets.")

try:
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
    logging.debug("Firebase Admin initialized successfully.")
except Exception as e:
    logging.error(f"Error initializing Firebase: {e}")
    st.error("Failed to initialize Firebase. Please check your configuration.")
    st.stop()

# Streamlit App
st.title("Firestore Data Viewer")

# Define your Firestore collection
collection_name = "dic_project"

# Fetch and display Firestore data
st.subheader("View Data from Firestore")
try:
    logging.debug(f"Fetching data from Firestore collection: {collection_name}")
    docs = db.collection(collection_name).stream()  # Fetch all documents
    data_list = [doc.to_dict() for doc in docs]  # Convert documents to a list of dictionaries

    if data_list:
        logging.debug(f"Fetched {len(data_list)} documents from Firestore.")
        st.write("Data in Firestore:")
        st.write(data_list)  # Display all data as a list of dictionaries
    else:
        logging.warning("No data found in the Firestore collection.")
        st.warning("No data found in the collection.")
except Exception as e:
    logging.error(f"Error fetching data from Firestore: {e}")
    st.error(f"Error fetching data from Firestore: {e}")
