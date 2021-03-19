import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.groupon.com/landing/deal-of-the-day']
    start_urls = ['https://www.groupon.com/landing/deal-of-the-day']

    def parse(self, response):
     
        for product in response.xpath('//div[@class="grpn-dc-caption"]'):
            yield{
                "title":product.xpath('.//div[@class="grpn-dc-title"]/text()').get(),
                "price":product.xpath('.//span[@class="wh-dc-price-discount c-txt-price"]/text()').get(),
                'rating':product.xpath('.//div[@class="grpn-total-ratings"]/text()').get()
            }
