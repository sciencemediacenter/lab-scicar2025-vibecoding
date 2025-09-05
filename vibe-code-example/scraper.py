"""Bundestag web scraper using ScrapeGraphAI."""

import csv
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph

from models import ScrapedDocument, Document


class BundestagScraper:
    """Bundestag document scraper using ScrapeGraphAI."""
    
    def __init__(self):
        """Initialize the scraper with OpenAI configuration."""
        load_dotenv()
        
        self.graph_config = {
            "llm": {
                "api_key": os.getenv("OPENAI_KEY"),
                "model": "openai/gpt-4o-mini",
            },
            "verbose": True,
            "headless": True,
        }
    
    def scrape_url(self, url: str, topic: str) -> ScrapedDocument:
        """Scrape a single URL and return structured data."""
        
        prompt = """
        Extract the following information from this Bundestag webpage:
        1. title: The main title of the document/article (usually the main heading)
        2. content: The main text content as clean text (preserve structure but remove HTML tags)
        3. author: Look specifically for "Herausgeber" section to find the author/publisher information
        4. documents: Look in the "Dokumente" section for document links with their titles and URLs (typically PDF files with Drucksache numbers)
        
        Return the information in JSON format with these exact keys: title, content, author, documents
        For documents, each item should have: title, url, file_type
        """
        
        # Create the SmartScraperGraph instance
        smart_scraper = SmartScraperGraph(
            prompt=prompt,
            source=url,
            config=self.graph_config
        )
        
        # Run the scraping
        result = smart_scraper.run()
        
        # Extract and process the data
        title = ""
        content = ""
        author = ""
        documents = []
        
        if result and isinstance(result, dict):
            # Handle different possible structures
            if 'content' in result and isinstance(result['content'], dict):
                content_data = result['content']
                title = content_data.get('title', '')
                
                # Handle content - try different keys
                if 'main_text_html' in content_data:
                    content = content_data['main_text_html']
                elif 'mainContent' in content_data:
                    content = content_data['mainContent']
                elif 'content' in content_data:
                    content = content_data['content']
                
                # Handle author
                author_info = content_data.get('author', content_data.get('authorInfo', content_data.get('author_info', '')))
                if isinstance(author_info, list) and author_info:
                    author = author_info[0].get('name', '') if isinstance(author_info[0], dict) else str(author_info[0])
                elif isinstance(author_info, str):
                    author = author_info
                
                # Handle documents
                doc_links = content_data.get('documents', content_data.get('downloads', content_data.get('downloadLinks', content_data.get('download_links', []))))
                if isinstance(doc_links, list):
                    for link in doc_links:
                        if isinstance(link, dict):
                            documents.append(Document(
                                title=link.get('title', ''),
                                url=link.get('url', link.get('link', '')),
                                file_type=link.get('file_type', link.get('fileType', 'PDF'))
                            ))
            else:
                # Direct structure
                title = result.get('title', '')
                content = result.get('content', '')
                author = result.get('author', '')
                
                # Handle documents
                doc_links = result.get('documents', result.get('download_links', []))
                if isinstance(doc_links, list):
                    for link in doc_links:
                        if isinstance(link, dict):
                            documents.append(Document(
                                title=link.get('title', ''),
                                url=link.get('url', link.get('link', '')),
                                file_type=link.get('file_type', link.get('fileType', 'PDF'))
                            ))
        
        # Ensure content is a string
        if not isinstance(content, str):
            content = str(content) if content else ""
        
        # Create ScrapedDocument
        scraped_doc = ScrapedDocument(
            topic=topic,
            title=title,
            text_html=content,
            author=author,
            documents=documents,
            scraped_at=datetime.now(),
            source_url=url
        )
        
        return scraped_doc
    
    def read_urls_csv(self, csv_path: str) -> List[Dict[str, str]]:
        """Read URLs and topics from CSV file."""
        urls_data = []
        
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                urls_data.append({
                    'url': row['url'],
                    'topic': row['topic']
                })
        
        return urls_data
    
    def scrape_all_urls(self, csv_path: str, output_path: str):
        """Scrape all URLs from CSV and save to JSON output."""
        
        # Read URLs from CSV
        urls_data = self.read_urls_csv(csv_path)
        
        scraped_documents = []
        
        print(f"Starting to scrape {len(urls_data)} URLs...")
        
        for i, url_data in enumerate(urls_data, 1):
            url = url_data['url']
            topic = url_data['topic']
            
            print(f"[{i}/{len(urls_data)}] Scraping: {url}")
            
            try:
                scraped_doc = self.scrape_url(url, topic)
                scraped_documents.append(scraped_doc)
                print(f"✅ Successfully scraped: {scraped_doc.title}")
                
            except Exception as e:
                print(f"❌ Error scraping {url}: {str(e)}")
                # Create a minimal document with error info
                error_doc = ScrapedDocument(
                    topic=topic,
                    title=f"Error scraping {url}",
                    text_html=f"Error: {str(e)}",
                    author="",
                    documents=[],
                    scraped_at=datetime.now(),
                    source_url=url
                )
                scraped_documents.append(error_doc)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Convert to dict for JSON serialization
        output_data = [doc.model_dump() for doc in scraped_documents]
        
        # Save to JSON
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(output_data, file, indent=2, ensure_ascii=False, default=str)
        
        print(f"📁 Saved {len(scraped_documents)} documents to {output_path}")
        

def main():
    """Main function to run the scraper."""
    
    # Paths
    base_dir = Path(__file__).parent
    csv_path = base_dir / "data" / "input" / "urls.csv"
    output_path = base_dir / "data" / "output" / "out.json"
    
    # Initialize and run scraper
    scraper = BundestagScraper()
    scraper.scrape_all_urls(str(csv_path), str(output_path))


if __name__ == "__main__":
    main()