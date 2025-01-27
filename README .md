# YouTube Scraper

A Python module to scrape YouTube videos based on a search query. The module allows users to filter videos based on whether they are music videos or live streams.

## Features

- Search YouTube for videos based on a query.
- Filter results to include only music videos, live streams, or general videos.
- Output URLs of relevant videos.

## Requirements

- Python 3.7+
- Google Chrome and ChromeDriver
- Python libraries: `selenium`, `webdriver-manager`

Install dependencies:

```bash
pip install selenium webdriver-manager
```

## Usage

### Example 1: General Results

Fetch general video URLs (not filtering for music or live videos):

```python
from yt_scp import youtube_scrape

query = "Python tutorials"
urls = youtube_scrape(query=query, max_results=5, music=False, live=False)
for i, url in enumerate(urls, start=1):
    print(f"Video {i}: {url}")
```

### Example 2: Music Videos Only

Fetch only music video URLs based on the query:

```python
from yt_scp import youtube_scrape

query = ""
urls = youtube_scrape(query=query, max_results=5, music=True, live=False)
for i, url in enumerate(urls, start=1):
    print(f"Music Video {i}: {url}")
```

### Example 3: Live Videos Only

Fetch only live video URLs based on the query:

```python
from yt_scp import youtube_scrape

query = ""
urls = youtube_scrape(query=query, max_results=5, music=False, live=True)
for i, url in enumerate(urls, start=1):
    print(f"Live Video {i}: {url}")
```

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
