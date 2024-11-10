import os
import openai
import pandas as pd
from flask import Flask, request, jsonify, render_template, send_file
from serpapi import GoogleSearch
from google.oauth2 import service_account
from googleapiclient.discovery import build
from io import BytesIO

app = Flask(__name__)

# Load API keys from environment variables
SERPAPI_KEY = "YOUR_SERPAPI_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY

# Google Sheets setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Route to render the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Route to upload CSV or connect to Google Sheets
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    sheet_url = request.form.get('sheetUrl')
    if file:
        data = pd.read_csv(file)
    elif sheet_url:
        spreadsheet_id = sheet_url.split('/')[5]
        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range="Sheet1").execute()
        values = result.get('values', [])
        data = pd.DataFrame(values[1:], columns=values[0])
    else:
        return jsonify({'error': 'No data source provided'}), 400
    return data.to_json()

# Route to process search and LLM parsing
@app.route('/search', methods=['POST'])
def search():
    data = pd.DataFrame(request.json.get('data'))
    column = request.json.get('column')
    prompt_template = request.json.get('prompt')
    results = []

    for entity in data[column]:
        query = prompt_template.replace('{entity}', entity)
        search_results = perform_search(query)
        parsed_data = parse_with_llm(search_results, prompt_template)
        results.append({'entity': entity, 'data': parsed_data})

    return jsonify(results)

# Helper to perform web search using SerpAPI
def perform_search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict().get("organic_results", [])
    return results

# Helper to parse search results with LLM
def parse_with_llm(results, prompt_template):
    combined_text = " ".join([result.get("snippet", "") for result in results])
    prompt = f"Based on the query '{prompt_template}', extract relevant information:\n{combined_text}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

# Route to download results as CSV
@app.route('/download', methods=['POST'])
def download():
    results = request.json.get('results')
    df = pd.DataFrame(results)
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, as_attachment=True, download_name='search_results.csv', mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)
