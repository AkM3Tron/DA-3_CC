Finance-Based CSV Chatbot

This chatbot is specifically designed for querying financial data stored in CSV files. It dynamically ingests data and allows users to ask contextual questions.

Features:

Upload CSV files for dynamic analysis.
Ask questions in plain text about the uploaded data.
Requirements:

Install the Llama framework.
Download and configure a suitable LLM model through the Llama ecosystem.
CSV file containing financial data.
How to Use:
Install and set up the LLM model locally.
Start the Flask server by running the Python script.
Upload a CSV file via a POST request to /upload_csv.
Ask questions by sending a POST request to /query_csv with the question as plain text in the request body.
Receive the response as plain text.
