import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text


# Function to execute SQL query and return result
def execute_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        if sql.strip().upper().startswith("SELECT"):
            rows = cur.fetchall()
            conn.close()
            return rows
        else:
            conn.commit()
            conn.close()
            return "Query executed successfully."
    except sqlite3.Error as e:
        return f"Error: {e}"


# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!

    The SQL database named STUDENT contains the following columns: NAME, CLASS, and SECTION.

    For example:

    1. To count the number of records in the database, you can ask:
    "How many entries are there in the database?"
    The SQL command would be:
    SELECT COUNT(*) FROM STUDENT;

    2. To retrieve all students studying in a specific class, you can ask:
    "List all students in the Data Science class."
    The SQL command would be:
    SELECT * FROM STUDENT WHERE CLASS = "Data Science";

    3. To find students with a certain grade or score, you can ask:
    "Show me students who scored above 90."
    The SQL command would be:
    SELECT * FROM STUDENT WHERE MARKS > 90;

    Remember, the SQL code should not be enclosed in triple backticks, and the word "sql" should not be present in the output.
    Ask your question, and I'll provide the corresponding SQL query!
    """
]

# Streamlit App
st.set_page_config(page_title="Gemini SQL Query Executor")

# Header and user input
st.header("Gemini App To Execute SQL Queries")
question = st.text_input("Input: ", key="input")
submit = st.button("Execute")

# if submit is clicked
if submit:
    # Generate response and retrieve SQL query
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")

    if response:
        st.code(response.strip(), language="sql")

        # Execute the SQL query
        result = execute_sql_query(response.strip(), "Chinook.db")

        # Display query result
        if result:
            if isinstance(result, str):
                st.info(result)
            else:
                st.subheader("Query Result:")
                st.table(result)
        else:
            st.warning("No data found for the provided query.")
    else:
        st.error("Failed to generate a response.")

# from dotenv import load_dotenv
# import streamlit as st
# import os
# import sqlite3
# import google.generativeai as genai
#
# # Load environment variables
# load_dotenv()
#
# # Configure Genai Key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#
#
# # Function to load Google Gemini Model and provide queries as response
# def get_gemini_response(question, prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([prompt[0], question])
#     return response.text
#
#
# # Function to retrieve query from the database
# def read_sql_query(sql, db):
#     try:
#         conn = sqlite3.connect(db)
#         cur = conn.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         conn.commit()
#         conn.close()
#         return rows
#     except sqlite3.Error as e:
#         st.error(f"Error occurred: {e}")
#         return []
#
#
# # Define Your Prompt
# prompt = [
#     """
#      You are an expert in converting English questions to SQL queries!
#
#   The SQL database named STUDENT contains the following columns: NAME, CLASS, and SECTION.
#
#   For example:
#
#   1. To count the number of records in the database, you can ask:
#      "How many entries are there in the database?"
#      The SQL command would be:
#      SELECT COUNT(*) FROM STUDENT;
#
#   2. To retrieve all students studying in a specific class, you can ask:
#      "List all students in the Data Science class."
#      The SQL command would be:
#      SELECT * FROM STUDENT WHERE CLASS = "Data Science";
#
#   3. To find students with a certain grade or score, you can ask:
#      "Show me students who scored above 90."
#      The SQL command would be:
#      SELECT * FROM STUDENT WHERE MARKS > 90;
#  pleses only give me query nothing else
#   Remember, the SQL code should not be enclosed in triple backticks, and the word "sql" should not be present in the output. Ask your question, and I'll provide the corresponding SQL query!
#
#       """
# ]
#
# # Streamlit App
# st.set_page_config(page_title="I can Retrieve Any SQL query")
#
# # Header and user input
# st.header("Gemini App To Retrieve SQL Data")
# question = st.text_input("Input: ", key="input")
# submit = st.button("Ask the question")
#
# # if submit is clicked
# if submit:
#     # Generate response and retrieve SQL query
#     response = get_gemini_response(question, prompt)
#     st.subheader("Generated SQL Query:")
#     st.code(response, language="sql")
#     if response.startswith("INSERT INTO STUDENT"):
#         # Remove triple backticks from the response
#         response = response.strip("`")
#         rows = read_sql_query(response, "Chinook.db")
#
#         # Display query result
#         if rows:
#             st.subheader("Query Result:")
#             for row in rows:
#                 st.write(row)
#         else:
#             st.warning("No data found for the provided query.")
#     else:
#         st.error("The generated query is not an INSERT statement.")
