import pandas as pd
from llama_index import GPTSimpleVectorIndex
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    file = request.files['file']
    df = pd.read_csv(file)
    df.to_csv('finance_data.csv', index=False)
    return "CSV uploaded successfully"

@app.route('/query_csv', methods=['POST'])
def query_csv():
    question = request.data.decode('utf-8')
    df = pd.read_csv('finance_data.csv')
    index = GPTSimpleVectorIndex.from_dataframe(df)
    response = index.query(question)
    return str(response)

if __name__ == '__main__':
    app.run(port=6000)
