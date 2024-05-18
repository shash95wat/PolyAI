import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="PolyAI",
    layout="wide"  # Opt for a wide layout
)

# Define main title
st.title("Welcome to PolyAI")

# Sidebar section
with st.sidebar:
    st.markdown("## Navigation")
    page_selection = st.radio("Go to", ["Home", "About"])

# Main content
if page_selection == "Home":
    st.header("Home Page")

    # Introduction
    st.write("""
    **PolyAI** is an AI-powered application designed to streamline communication and data management tasks. 
    It features:
    - **PDF Chat:** A feature allowing users to interact with PDF documents using natural language.
    - **ATS System:** An Applicant Tracking System for efficient recruitment processes.
    - **SQL Chat:** An interface for querying and manipulating SQL databases using conversational language.
    """)

    # Technology Details
    st.subheader("Technology Details")
    st.write("""
    PolyAI is developed using Langchain and Gemini, cutting-edge technologies for natural language processing and AI development.
    - **Langchain:** Langchain is a powerful framework for NLP tasks, enabling advanced language understanding and processing.
    - **Gemini:** Gemini is an AI language model that powers PolyAI's conversational capabilities, allowing users to interact with the application using natural language.
    """)

    # Explore Functionalities
    st.subheader("Explore Functionalities")
    st.write("""
    Feel free to explore the various functionalities of PolyAI by selecting different options from the sidebar navigation menu.
    """)

elif page_selection == "About":
    st.header("About Page")

    # Project Overview
    st.write("""
    **PolyAI** is developed using Langchain, a cutting-edge technology for natural language processing and AI development. 
    It aims to revolutionize how users interact with data and streamline complex tasks through intuitive interfaces and AI capabilities.
    """)

    # Technologies Used
    st.subheader("Technologies Used")
    st.write("""
    - **Langchain:** Langchain is a powerful framework for NLP tasks, enabling advanced language understanding and processing.
    - **Gemini:** Gemini is an AI language model that powers PolyAI's conversational capabilities, allowing users to interact with the application using natural language.
    """)

