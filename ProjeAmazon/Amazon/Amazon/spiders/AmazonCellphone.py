import scrapy


class AmazoncellphoneSpider(scrapy.Spider):
    name = 'AmazonCellphone'
    allowed_domains = ['www.amazon.com.tr']
    start_urls = ['https://www.amazon.com.tr/s?k=Cep+Telefonu&i=electronics&rh=n%3A13709907031%2Cp_89%3AApple%7CGENERAL+MOBILE%7COPPO%7COppo+realme%7CSamsung&dc&qid=1630879073&rnid=13493765031&ref=sr_nr_p_89_6']

    def parse(self, response):
        CellPhones = response.xpath("//div[@class='a-section a-spacing-medium']/div[@class='a-section a-spacing-none']")
        for element in CellPhones:
            CellPhoneName =  element.xpath(".//div[@class='a-section a-spacing-none a-spacing-top-small']/h2/a/span/text()").get()
            CellPhonePrice = element.xpath(".//div[@class='a-section a-spacing-none a-spacing-top-small']/div/a/span/span/text()").get()
            yield {
                'product_name': CellPhoneName,
                'product_price': CellPhonePrice}
        
        PageNext = response.xpath("//div[@class='a-section a-spacing-none a-padding-base']/div/ul/li[@class='a-last']/a/@href").get()

        if PageNext:
            Link = response.urljoin(PageNext)
            yield scrapy.Request(url=Link,callback=self.parse)


            
"""kodu, scrapy crawl AmazonCellphone -o amazoncellphone.json komutu ile çalıştırınız"""        