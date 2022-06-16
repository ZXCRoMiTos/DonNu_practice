import scrapy
import re


class NixSpider(scrapy.Spider):
    name = 'nix'
    allowed_domains = ['nix.dn.ua']
    start_urls = ['https://nix.dn.ua/']

    @staticmethod
    def filter_links(links):
        return [link for link in links if link.count('/') == 3]

    @staticmethod
    def parse_product(response):
        yield {
            "title": response.css("h1.heading span::text").get(),
            "price": response.css("span.autocalc-product-price::text").get(),
            "category": '/'.join(response.css('ul.breadcrumb li a::text').extract()),
            "url": response.url
        }

    def parse_catalog(self, response):
        links = response.css("div.caption a::attr(href)")
        for link in links:
            yield response.follow(link, self.parse_product)

    def parse_pages_of_catalog(self, response):
        request = response.css('div.pagination_wrap div.text-right::text').get()
        number_of_pages = int(re.findall('\d+', request)[-1])
        for num in range(number_of_pages + 1):
            link = response.url + f"?page={num}"
            yield response.follow(link, self.parse_catalog)

    def parse(self, response):
        unfiltered_links = response.css("nav.navbar a::attr(href)").extract()
        links = self.filter_links(unfiltered_links)
        for link in links:
            yield response.follow(link, self.parse_pages_of_catalog)
