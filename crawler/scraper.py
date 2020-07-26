import time
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

class Scraper:
  @classmethod
  def get_robot_txt(cls, url):
    try:
      rp = RobotFileParser()
      parsed_url = urlparse(url)
      robots_url = "{0.scheme}://{0.netloc}/robot.txt".format(parsed_url)
      rp.set_url(robots_url)
      rp.read()
      return rp.can_fetch("*", url)
    except Exception as e:
      raise Exception(e.args[0])
  
  @classmethod
  def get_html(cls, url, params=None, headers=None):
    try:
      time.sleep(5)
      resp = requests.get(url, params=params, headers=headers)
      resp.encoding = resp.apparent_encoding
      soup = BeautifulSoup(resp.text, "html.parser")
      return soup
    except Exception as e:
      raise Exception(e.args[0])