from scrapy import Spider
from sublet_WebCrawler.items import SubletWebcrawlerItem

class spiderSublet(Spider):
    name = 'crawlSublet'
    start_urls = [
    'https://www.sublet.com/property/4323668',
    'https://www.sublet.com/property/2874327',
    'https://www.sublet.com/property/2874325',
    'https://www.sublet.com/property/4641200',
    'https://www.sublet.com/property/3178307',
    'https://www.sublet.com/property/3178306',
    'https://www.sublet.com/property/282927',
    'https://www.sublet.com/property/2814732',
    'https://www.sublet.com/property/3369402',
    'https://www.sublet.com/property/2840114',
    'https://www.sublet.com/property/2329730',
    'https://www.sublet.com/property/2808945',
    'https://www.sublet.com/property/2329753',
    'https://www.sublet.com/property/2275158',
    'https://www.sublet.com/property/2556624',
    'https://www.sublet.com/property/2520945',
    'https://www.sublet.com/property/145327',
    'https://www.sublet.com/property/286054',
    'https://www.sublet.com/property/2440166',
    'https://www.sublet.com/property/1850615',
    'https://www.sublet.com/property/2725483',
    'https://www.sublet.com/property/2526138',
    'https://www.sublet.com/property/2573717',
    'https://www.sublet.com/property/2561541',
    ]
    def parse(self,response):
        webItem = SubletWebcrawlerItem()
        webItem['id'] = None
        webItem['Url'] = response.url
        webItem['Description'] = None
        webItem['Rental'] = None
        webItem['Rent'] = None
        webItem['Location'] = None
        webItem['Lease'] = None
        webItem['Amenities'] = None
        webItem['Not_Included'] = None

        if response.url in self.start_urls:
            webItem['Rental'] = response.css('section.mb-2:nth-child(1)::text').getall()
            webItem['Rent'] = response.css('section.mb-2:nth-child(2)::text').getall()
            webItem['Location'] = response.css('section.mb-2:nth-child(3)::text').getall()
            webItem['Lease'] = response.css('section.mb-2:nth-child(4)::text').getall()
            webItem['Amenities'] = response.css('div.col-12.col-sm-6 ul.list-unstyled.amenities-yes li span::text').getall()
            webItem['Not_Included'] = response.css('div.col-12.col-sm-6 ul.list-unstyled li span s::text').getall()
        yield webItem 


