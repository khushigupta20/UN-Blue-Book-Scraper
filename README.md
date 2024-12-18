# UN Blue Book Scraper

This repository contains a web scraper designed to extract information from the [UN Blue Book](https://www.un.org/dgacm/en/content/blue-book). The Blue Book provides detailed information about Permanent Missions to the United Nations, including contact details and organizational data.

## Features

- Scrapes the **UN Blue Book** for publicly available mission data.
- Parses and organizes information for easy analysis.
- Outputs data in a structured format (e.g., CSV, JSON).

---

## How It Works

### 1. **Fetching Data**  
The scraper uses Python's **requests** library to send HTTP GET requests to the UN Blue Book's website and retrieve the HTML content of the relevant pages.

### 2. **Parsing HTML**  
The retrieved HTML is parsed using **BeautifulSoup**, a popular Python library for web scraping. The scraper locates specific HTML elements and attributes to extract relevant information (e.g., country names, mission details, contact information).

### 3. **Data Cleaning and Structuring**  
The extracted data is cleaned and structured into a standardized format. This includes handling missing values, removing redundant information, and ensuring consistency in formatting.

### 4. **Storing Data**  
The cleaned data is saved in user-specified formats such as:
   - **CSV**: For spreadsheet applications.
   - **JSON**: For easy integration with other tools or APIs.

### 5. **Error Handling**  
The script incorporates error-handling mechanisms to deal with:
   - Network issues (e.g., timeouts, failed requests).
   - Changes in the website structure (e.g., missing or updated HTML elements).

---

## Why Use https://bluebook.unmeetings.org/data.json Directly?

The scraper directly accesses the JSON endpoint https://bluebook.unmeetings.org/data.json rather than scraping the main page (https://bluebook.unmeetings.org/) for several reasons:

### 1. **Data Accessibility**  
The JSON file provides the complete dataset in a machine-readable format, eliminating the need to parse HTML. This ensures:
   - Cleaner and more straightforward data extraction.
   - Reduced risk of errors caused by changes in the HTML structure of the website.

### 2. **Efficiency**  
By directly fetching the JSON file:
   - The scraper avoids making multiple requests to load and parse individual HTML elements.
   - The process is faster and less resource-intensive.

### 3. **Structured Data**  
The JSON file contains data in a structured format, with fields like country name, mission details, and contact information already organized. This simplifies data processing as the need for additional cleaning or restructuring is minimized.

### 4. **Stability**  
HTML scraping is prone to breaking if the website layout or structure changes. In contrast, JSON endpoints are typically designed for data consumption by applications and are less likely to change frequently.

### Example Comparison:
- **Using HTML Scraping**:  
   The scraper would need to:
   - Download the entire web page.
   - Identify and extract relevant information from various HTML tags (e.g., div, table).  
   This approach is slower, error-prone, and dependent on the consistency of the website's structure.
- **Using the JSON Endpoint**:  
   The scraper downloads a single JSON file containing all the required data, eliminating the complexity of parsing the HTML.

### 5. **Official Endpoint**  
The JSON file is hosted at the same domain as the main website, indicating that it is an official data source intended for programmatic access. This avoids violating the website's terms of service.

---

### Example Workflow:
- The user runs the script by executing:
 ```
  bash
  python scraper.py
 ```
- The script fetches the data, processes it, and saves the output in the desired format.

---

## Prerequisites

Before running the scraper, ensure you have the following installed:

- **Python** (version 3.7 or higher)
- Necessary Python libraries listed in requirements.txt.

---

## Installation

1. Clone the repository:
 ```
  git clone https://github.com/khushigupta20/UN-Blue-Book-Scrapper.git
  cd UN-Blue-Book-Scrapper
 ```
2. Install dependencies:
 ```
  pip install -r requirements.txt
 ```
---

## Usage

1. Run the scraper:
 ```
  python scraper.py
 ```
2. Specify the output format and file location (if applicable).

3. View the extracted data in the chosen format.

---

## Output

The scraper generates the extracted data in a user-specified format, such as:

- **CSV**: A spreadsheet-ready file.
- **JSON**: A flexible format for integration with other tools.

