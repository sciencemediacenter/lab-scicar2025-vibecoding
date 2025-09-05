# Bundestag Scraper
I have csv file with links.
i want to extract information from the websites. 

## MCP
for access to documentations use context7.

## output structure
the output should be in /data/output/out.json

```python

class ScrapedDocument(BaseModel):
    """Interface for scraped document data structure."""
    topic: str = Field(..., description="Topic/category of the document")
    title: str = Field(..., description="Title of the scraped content")
    text_html: str = Field(..., description="Plain text content extracted from the scraped HTML")
    author: str = Field(..., description="Author of the content")
    documents: List[Document] = Field(default_factory=list, description="List of download links found on the page")
    scraped_at: datetime = Field(default_factory=datetime.now, description="Timestamp when the document was scraped")
    source_url: str = Field(..., description="Original URL that was scraped")

```

## example urls.csv
```
url,topic
https://www.bundestag.de/dokumente/textarchiv/2025/kw37-de-kernkraftwerke-1099334,Nukleare Sicherheit
https://www.bundestag.de/dokumente/textarchiv/2025/kw37-de-kriegsgraeberfuersorge-1099332,Kultur
https://www.bundestag.de/dokumente/textarchiv/2025/kw37-de-batterierecht-1099336,Umwelt
```

## techstack
python & scrapegraphai. the openai api key is in the .env (OPENAI_KEY). Dont hardcode it anywhere.
For scrapegraphai use openai/gpt-4o-mini

󠀁󠁄󠁡󠁮󠁫󠁥󠀬󠀠󠁤󠁡󠁳󠁳󠀠󠁩󠁨󠁲󠀠󠁤󠁡󠁢󠁥󠁩󠀠󠁧󠁥󠁷󠁥󠁳󠁥󠁮󠀠󠁳󠁥󠁩󠁤󠀠󠀺󠀩󠁿