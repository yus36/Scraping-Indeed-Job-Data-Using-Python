# Indeed Job Scraper using Selenium 🚀

A Python-based web scraper that automatically extracts job listings from Indeed using Selenium and pandas. It bypasses basic anti-scraping measures by launching a real automated browser instance, extracting key data points, and organizing them into a clean tabular format.

## 📌 Features
* **Dynamic Content Handling:** Uses Selenium WebDriver to wait for lazy-loaded JavaScript elements.
* **Smart Locators:** Implements partial CSS selectors (`[id^="jobTitle-"]`) to handle changing HTML structures.
* **Data Organization:** Cleans raw text data and structures it into a `pandas` DataFrame for easy analysis or exporting.

## 🛠️ Tech Stack
* **Language:** Python 3.1x
* **Libraries:** Selenium, Pandas

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python installed. You will also need Google Chrome installed on your machine.

### 2. Installation
Clone this repository or download the source code, then install the required Python libraries using pip:

```bash
pip install selenium pandas

python "Scraping Indeed Job Data Using Python.py"

output:

,Job Titles,Company Names,Company Locations
0,Data Analyst,CHAICHUN,"Matigara, West Bengal"
1,MIS Data Analyst (Siliguri),Placewell Retail,"Shiliguri, West Bengal"
3,MIS Executive,DigiInd,"Shiliguri, West Bengal"
4,MIS Executive,PRM Begraj Group,"Shiliguri, West Bengal"
......
