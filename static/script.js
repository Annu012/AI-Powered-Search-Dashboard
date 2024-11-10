// Upload file and fetch column data
async function uploadFile() {
    const fileInput = document.getElementById("fileInput").files[0];
    const sheetUrl = document.getElementById("sheetUrlInput").value;
    const formData = new FormData();
    if (fileInput) formData.append("file", fileInput);
    else formData.append("sheetUrl", sheetUrl);
  
    const response = await fetch("/upload", { method: "POST", body: formData });
    const data = await response.json();
    populateColumnSelect(Object.keys(data[0]));
  }
  
  // Populate column select dropdown
  function populateColumnSelect(columns) {
    const columnSelect = document.getElementById("columnSelect");
    columnSelect.innerHTML = columns.map(col => `<option value="${col}">${col}</option>`).join("");
  }
  
  // Perform search based on user-defined prompt
  async function performSearch() {
    const column = document.getElementById("columnSelect").value;
    const prompt = document.getElementById("promptInput").value;
    const data = { column, prompt };
  
    const response = await fetch("/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
  
    const results = await response.json();
    displayResults(results);
  }
  
  // Display results on page
  function displayResults(results) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = results.map(result => `<p><b>${result.entity}:</b> ${result.data}</p>`).join("");
  }
  
  // Download results as CSV
  async function downloadResults() {
    const response = await fetch("/download", { method: "POST", headers: { "Content-Type": "application/json" } });
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "search_results.csv";
    link.click();
  }
  