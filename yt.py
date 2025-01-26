from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
#import yt_summ

def youtube_scrape(query, max_results=10):
    """
    Scrapes YouTube search results for titles, descriptions, URLs, and video durations using Selenium.
    
    :param query: Search query string.
    :param max_results: Number of results to fetch (default is 10).
    :return: List of URLs for videos with durations <= 10 minutes.
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
        # Construct the search URL with "news under 10 min"
        search_query = f"{query} news under 10 min"
        search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
        driver.get(search_url)
        time.sleep(3)  # Wait for the page to load

        # Find video elements
        video_elements = driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer, ytd-compact-video-renderer")
        results_urls = []

        for video in video_elements[:max_results]:
            title_element = video.find_element(By.CSS_SELECTOR, "h3 a")
            title = title_element.text
            url = title_element.get_attribute("href")
            
            # Check for regular video duration
            try:
                duration_element = video.find_element(By.CSS_SELECTOR, "span.ytd-thumbnail-overlay-time-status-renderer")
                duration = duration_element.text.strip()
            except:
                duration = None  # No duration for Shorts

            # If the duration exists and is 10 minutes or less, or if it's a YouTube Short (no duration but acceptable)
            if duration and "m" in duration:  # Ensure the duration contains minutes
                minutes = int(duration.split("m")[0].strip())
                if minutes <= 10:
                    results_urls.append(url)
            elif not duration:  # Handle Shorts without duration
                results_urls.append(url)

        return results_urls

    finally:
        driver.quit()

if __name__ == "__main__":
    query = input("Enter search query: ")
    max_results = int(input("Enter the number of results to fetch: "))

    try:
        video_urls = youtube_scrape(query, max_results)
        print("\nURLs of videos with durations under 10 minutes or Shorts:\n")
        for idx, url in enumerate(video_urls, start=1):
            print(f"{idx}. URL: {url}\n")
        # Now you can pass `video_urls` to `yt_summ.process_videos`
       # results = yt_summ.process_videos(video_urls)
        
        ## Optionally, save results to a file
        #output_file = "transcription_results.txt"
        #with open(output_file, "w", encoding="utf-8") as f:
        #    for url, result in results.items():
        #        f.write(f"Video URL: {url}\n")
        #        f.write(f"Transcript:\n{result['transcript']}\n")
        #        f.write(f"Sentiment Analysis:\n{result['sentiment']}\n")
        #        f.write(f"Transcription File: {result['transcription_file']}\n")
        #        f.write("\n---\n")
#
        #print(f"Results saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")
