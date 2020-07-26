from crawler_google import CrawlerGoogle

class CrawlerFactory:
  @classmethod
  def create(cls, engine):
    if engine == "google":
      return CrawlerGoogle()
    else:
      raise Exception("No Engine")