import time
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from logging import basicConfig, getLogger, DEBUG, INFO
from scraper import Scraper
from ua import UserAgent
from crawler_factory import CrawlerFactory
from crawler_parameter import CrawlerParameter

formatter = "[%(asctime)s][%(name)s][%(levelname)s]%(message)s"
basicConfig(level=INFO, format=formatter)

class Crawler:
  def __init__(self, engine="google"):
    self.engine = engine
  
  def get_search_url(self, params):
    logger = getLogger("get_search_url()")
    try:
      c = CrawlerFactory.create(self.engine)
      return c.crawl(params)
    except Exception as e:
      logger.warning(e)
      return None


if __name__ == "__main__":
  try:
    crawler = Crawler()
    params = CrawlerParameter("νガンダム", UserAgent.robot)
    urls = crawler.get_search_url(params)
    if urls != None:
      for url in urls:
        if Scraper.get_robot_txt(url):
          soup = Scraper.get_html(url)
          print(soup.title.get_text())
        else:
          print("クロールが拒否されました [{}]".format(url))
    else:
      print("取得できませんでした")
  except Exception as e:
    print ("error!")
