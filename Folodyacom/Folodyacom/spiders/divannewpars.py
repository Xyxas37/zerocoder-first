import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]


    def parse(self, response):

        svets = response.css("div.LlPhw")

        for svet in svets:
            yield {
                "name" : svet.css("div.lsooF::text").get(),
                "price" : svet.css("div.ui-LD-ZU KIkOH::text").get(),
                "url" : svet.css("a").attrib["href"]
            }