import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    # Указываем User-Agent
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    def parse(self, response):
        # Проверяем структуру HTML и корректируем селекторы
        svets = response.css("div.LlPhw")  # Подберите актуальный класс

        for svet in svets:
            yield {
                "name" : svet.css("span.lsooF::text").get(),  # Корректный селектор названия
                "price" : svet.css("span.pY3d2::text").get(),  # Добавляем цену
                "url" : svet.css("a").attrib["href"]  # Добавляем ссылку на товар
            }
            print("name")
            print("price")
