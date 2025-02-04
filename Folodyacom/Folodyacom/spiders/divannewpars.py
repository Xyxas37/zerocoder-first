import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]


    def parse(self, response):
        # Проверяем структуру HTML и корректируем селекторы
        svets = response.css("div.LlPhw")  # Подберите актуальный класс

        for svet in svets:
            yield {
                "name" : svet.css("div.lsooF::text").get(),  # Корректный селектор названия
                "price" : svet.css("div.ui-LD-ZU KIkOH::text").get(),  # Добавляем цену
                "url" : svet.css("a").attrib["href"]  # Добавляем ссылку на товар
            }