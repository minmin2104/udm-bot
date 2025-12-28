from botasaurus.browser import browser, Driver
import json
from bs4 import BeautifulSoup
from botasaurus.soupify import soupify


def get_title(soup: BeautifulSoup):
    title_tag = soup.find('h1', attrs={'data-purpose': 'lead-title'})
    title = title_tag.get_text()
    return title


@browser(
        parallel=2,
        max_retry=3,
        )
def scrape(driver: Driver, data):
    driver.google_get(data)
    driver.short_random_sleep()

    html = driver.page_html
    soup = soupify(html)
    title = get_title(soup)
    return {
            "Title": title
            }


if __name__ == "__main__":
    path = "sample.json"
    data = []
    with open(path, "r") as f:
        data = json.load(f)
    scrape(data)
