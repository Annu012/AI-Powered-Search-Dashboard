AI-Powered Search Dashboard

"This project is a web-based application that allows users to upload a dataset (CSV or Google Sheet), define search queries with dynamic placeholders, and retrieve relevant information for each entity in a selected column. The app uses SerpAPI for web search and OpenAI's GPT-4 (or another LLM) to parse the search results and extract structured information based on the user-defined query."

**Features**

1 .Upload Dataset: Supports CSV file uploads or Google Sheets for data input.

2 .Customizable Search Prompts: Allows users to define search prompts with placeholders for dynamic queries.

3 .Automated Web Search: Uses SerpAPI to perform searches for each entity.

4 .LLM Parsing: Leverages OpenAI's GPT-4 to parse and structure data from web search results.

5 .Results Download: Download structured search results as a CSV file.

**Prerequisites**

*SerpAPI API Key*: Sign up at SerpAPI and obtain an API key.

*OpenAI API Key*: Obtain an API key from OpenAI.

*Google Sheets API*: If using Google Sheets, enable the Google Sheets API in the Google Cloud Console and download your credentials.json file.


**Usage**

1.Upload Data:
   Upload a CSV file or provide a Google Sheets URL.
   Once the data loads, select the main column containing entities for the search (e.g., "company").

2.Define Search Prompt
   Enter a search prompt with placeholders, e.g., "Find the email address of {entity}".
   The {entity} placeholder will be replaced by each value in the selected column.

3.Start Search

  Click "Start Search" to initiate the automated search process.
  The system will perform searches using SerpAPI and parse the results with OpenAI’s API.

4.View and Download Results
  The results will display on the page.
  Click "Download Results" to save the structured output as a CSV file.

**Technologies Used**

*Flask*: Backend framework to handle API requests and serve the frontend.

*SerpAPI*: Used for automated Google searches.

*OpenAI API*: Leverages GPT-4 to parse and structure search results.

*Pandas*: For handling CSV files and data processing.

*Google Sheets API*: To read data directly from Google Sheets if provided.

**Important Notes**

Rate Limits: Be mindful of API rate limits for both SerpAPI and OpenAI. Adjust rate limiting in app.py if needed.

Environment Variables: Keep your .env file secure as it contains sensitive API keys.

Error Handling: Basic error handling is implemented, but ensure that CSV or Google Sheet data is well-structured.



License

This project is licensed under the MIT License.