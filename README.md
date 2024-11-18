# AI-Powered Search Dashboard

## Overview
The **AI-Powered Search Dashboard** is a web-based application designed to enhance data-driven insights by automating web searches and structuring results. This app allows users to upload datasets, define dynamic search prompts, and retrieve structured information using SerpAPI and OpenAI's GPT-4 (or another LLM). The results can then be downloaded in a CSV format for further analysis.

---

## Features
1. **Upload Dataset:**  
   Upload data from a CSV file or directly via a Google Sheets URL for processing.
   
2. **Customizable Search Prompts:**  
   Define search prompts with placeholders for dynamic queries, such as `Find the email address of {entity}`.

3. **Automated Web Search:**  
   Use SerpAPI to perform automated searches for each entity in a selected dataset column.

4. **LLM Parsing:**  
   Utilize OpenAI’s GPT-4 to extract and structure relevant data from web search results.

5. **Results Download:**  
   Download structured search results as a CSV file for offline use.

---

## Prerequisites
To use the application, ensure you have the following:
1. **SerpAPI API Key:**  
   Sign up at [SerpAPI](https://serpapi.com/) and obtain an API key.
   
2. **OpenAI API Key:**  
   Obtain your API key from [OpenAI](https://openai.com/).
   
3. **Google Sheets API Credentials (optional):**  
   - Enable the Google Sheets API in the [Google Cloud Console](https://console.cloud.google.com/).  
   - Download your `credentials.json` file for accessing Google Sheets.

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/ai-powered-search-dashboard.git
   cd ai-powered-search-dashboard
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the project root with the following:
     ```
     SERPAPI_KEY=your_serpapi_key
     OPENAI_API_KEY=your_openai_key
     GOOGLE_SHEETS_CREDENTIALS=path/to/credentials.json
     ```

4. Run the application:
   ```bash
   python app.py
   ```
   The application will run locally at `http://localhost:5000`.

---

## Usage
1. **Upload Data:**  
   - Upload a CSV file or provide a Google Sheets URL.  
   - Select the column containing the entities you want to search for (e.g., `company`).

2. **Define Search Prompt:**  
   - Enter a prompt with a placeholder `{entity}` for dynamic queries.  
     Example: `Find the LinkedIn profile of {entity}`.

3. **Start Search:**  
   - Click **Start Search** to perform automated searches using SerpAPI.  
   - The system will process results using GPT-4 to extract and structure relevant information.

4. **View and Download Results:**  
   - View the structured search results on the dashboard.  
   - Click **Download Results** to save the output as a CSV file.

---

## Technologies Used
- **Flask:** Backend framework for serving the web application.  
- **SerpAPI:** API for performing automated web searches.  
- **OpenAI API:** GPT-4 integration for parsing and structuring search results.  
- **Pandas:** For handling and processing CSV data.  
- **Google Sheets API:** For reading data directly from Google Sheets.  

---

## Notes
- **Rate Limits:**  
  Be mindful of rate limits for both SerpAPI and OpenAI. Adjust rate-limiting settings in `app.py` as necessary.

- **Environment Variables:**  
  Keep your `.env` file secure as it contains sensitive API keys.

- **Error Handling:**  
  Ensure that your dataset is well-structured to avoid issues during processing.

---

## License
This project is licensed under the MIT License.

---

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with detailed explanations for your changes.  

---

## Contact
For any questions or support, feel free to reach out at [anisa.shaikh01@gmail.com].  
