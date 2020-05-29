# -*- coding: utf-8 -*-
import scrapy


class CntrydataSpider(scrapy.Spider):
    name = 'cntrydata'
    # allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    def parse(self, response):
        linkxp = '//div[@id="results"]/table//div/a/@href'
        linklist = response.xpath(linkxp)
        yield from response.follow_all(linklist, self.parsedata)

        nextpage = response.xpath('//div[@id="pagination"]/a/@href').get()
        if nextpage is not None:
            # nextpage = response.urljoin(nextpage)
            # yield scrapy.Request(nextpage, callback=self.parse)
            yield response.follow(nextpage, callback=self.parse)

    def parsedata(self, response):
        area = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_area__row"]//td/text()').get()
        population = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_population__row"]//td/text()').get()
        iso = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_iso__row"]//td/text()').get()
        country = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_country__row"]//td/text()').get()
        capital = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_capital__row"]//td/text()').get()
        continent = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_continent__row"]/td//text()').get()
        tld = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_tld__row"]//td/text()').get()
        curcod = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_currency_code__row"]//td/text()').get()
        curnam = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_currency_name__row"]//td/text()').get()
        phone = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_phone__row"]//td/text()').get()
        pcf = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_postal_code_format__row"]//td/text()').get()
        pcr = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_postal_code_regex__row"]//td/text()').get()
        lang = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_languages__row"]//td/text()').get()
        nebr = response.xpath('//div[@class="span12"]/form/table//tr[@id="places_neighbours__row"]//td[@class="w2p_fw"]/div/a/text()').getall()
        yield {
            country:[{"capital":capital},{"Population":population},{"Area":area},{"Iso":iso},{"Continent":continent},{"Tld":tld},{"Currency Code":curcod},{"Currency Name":curnam},{"Phone":phone},{"Postal Code Format":pcf},{"Postal Code Regex":pcr},{"Language":lang},{"Neighbour":nebr}]
        }

        