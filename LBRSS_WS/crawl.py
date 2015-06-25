from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import signals
from scrapy.utils.project import get_project_settings

def crawl():
	# runner = Crawler(get_project_settings())
	# runner.signals.connect(reactor.stop, signal=signals.spider_closed)
	# runner.configure()
	# spider = runner.spiders.create('crawl_news')
	# runner.crawl(spider)
	# runner.start()
	# reactor.run()
	print 1

if __name__ == '__main__':
	crawl()
