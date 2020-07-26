from crawler_base import CrawlerBase
from bs4 import BeautifulSoup
from scraper import Scraper

class CrawlerGoogle(CrawlerBase):
  def crawl(self, params):
    search_url = "https://www.google.co.jp/search"
    search_params = {"q": params.word}
    search_headers = {"User-Agent": params.user_agent}
    soup = Scraper.get_html(search_url, search_params, search_headers)
    if soup != None:
      meta = soup.findAll("meta", attrs={"name":"robots"}, content=lambda x: "nofollow" in str(x).lower() or "noarchive" in str(x).lower())
      if (len(meta) > 0):
        return None
      tags = soup.select(".r > a", href=True, rel=lambda x: "nofollow" not in str(x).lower())
      urls = [tag.get("href") for tag in tags]
      return urls
    else:
      raise Exception("No Data")