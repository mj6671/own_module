from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def youtube_scrape(query: str, max_results: int, music: bool, live: bool):
    """
    Scrape YouTube video URLs based on the query.
    
    Args:
        query (str): The search query for YouTube.
        max_results (int): Maximum number of results to fetch.
        music (bool): Whether to include only music videos.
        live (bool): Whether to include only live videos.
    
    Returns:
        list: List of URLs matching the filters.
    """
    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Construct the search URL
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        driver.get(search_url)
        time.sleep(3)  # Wait for the page to load

        # Find video elements
        video_elements = driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer, ytd-compact-video-renderer")
        results_urls = []

        for video in video_elements[:max_results]:
            # Extract title and URL
            title_element = video.find_element(By.CSS_SELECTOR, "h3 a")
            title = title_element.text
            url = title_element.get_attribute("href")
            
            # Extract duration or live status
            try:
                duration_element = video.find_element(By.CSS_SELECTOR, "span.ytd-thumbnail-overlay-time-status-renderer")
                duration = duration_element.text.strip()
            except:
                duration = None  # No duration means it might be a live video

            # Check for live videos
            is_live = "LIVE" in (duration.upper() if duration else "")

            # Apply filters
            if live and is_live:
                results_urls.append(url)
            elif music and not is_live:
                # Check for music keywords in the title
                music_keywords = ["official video", "lyrics", "song", "album"]
                if any(keyword.lower() in title.lower() for keyword in music_keywords):
                    results_urls.append(url)
            elif not music and not live and not is_live:
                # General case: include if neither music nor live is specifically requested
                results_urls.append(url)

        return results_urls

    finally:
        driver.quit()
