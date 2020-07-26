from abc import ABCMeta, abstractmethod

class CrawlerBase(metaclass=ABCMeta):
  @abstractmethod
  def crawl(self, params):
    pass