import unittest
from crawler import Crawler

class TestCrawler(unittest.TestCase):
  def test_get_robots_txt(self):
    crawler = Crawler()
    self.assertEqual(crawler.get_robot_txt("https://note.com"), True)
  
if __name__ == "__main__":
  unittest.main()
