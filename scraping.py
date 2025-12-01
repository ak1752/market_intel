import requests
from bs4 import BeautifulSoup

def scrape_sec_filings(ticker="AAPL", num_filings=5):
    """Scrape recent SEC filings for a company."""
    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    filings = []
    for row in soup.select("table.tableFile2 tr")[:num_filings]:
        cells = row.find_all("td")
        if len(cells) > 3:
            filings.append({
                "date": cells[0].text,
                "type": cells[1].text,
                "title": cells[2].text,
                "link": f"https://www.sec.gov{cells[2].find('a')['href']}"
            })
    return filings

def scrape_crunchbase(query="PLM", num_results=5):
    """Scrape Crunchbase for M&A or funding news (simplified)."""
    # Note: Crunchbase requires API key for full access; this is a mockup.
    return [
        {"title": f"Sample {query} Startup Raises $10M", "date": "2025-10-01", "description": "A startup in the PLM space raised $10M in Series A funding."},
        {"title": f"Acquisition in {query} Space", "date": "2025-09-15", "description": "Company X acquired Company Y to expand its CAD offerings."}
    ]
