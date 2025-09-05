# Bundestag Scraper

A web scraper built with ScrapeGraphAI to extract information from Bundestag documents.

## Features

- Scrapes URLs from a CSV file with topics
- Extracts structured information from Bundestag webpages
- Uses OpenAI GPT-4o-mini for intelligent content extraction
- Outputs results in JSON format matching the required structure

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare your CSV file with URLs and topics in `data/input/urls.csv`:
   ```csv
   url,topic
   https://www.bundestag.de/dokumente/textarchiv/2025/kw37-de-kernkraftwerke-1099334,Nukleare Sicherheit
   ```

2. Set your OpenAI API key in the `.env` file:
   ```
   OPENAI_KEY=your_openai_api_key_here
   ```

3. Run the scraper:
   ```bash
   python3 scraper.py
   ```

4. Results will be saved to `data/output/out.json`

## Output Structure

Each scraped document follows this structure:

```json
{
  "topic": "Nukleare Sicherheit",
  "title": "Moratorium für den Rückbau abgeschalteter Kernkraftwerke",
  "text_html": "Main content text...",
  "author": "Deutscher Bundestag, Internetredaktion",
  "documents": [
    {
      "title": "Document title",
      "url": "https://example.com/document.pdf",
      "file_type": "PDF"
    }
  ],
  "scraped_at": "2025-09-05 12:10:49.681045",
  "source_url": "https://original-url.de"
}
```

## Files

- `scraper.py`: Main scraper implementation
- `models.py`: Data models using Pydantic
- `requirements.txt`: Python dependencies
- `data/input/urls.csv`: Input CSV with URLs and topics
- `data/output/out.json`: Output JSON file with scraped data