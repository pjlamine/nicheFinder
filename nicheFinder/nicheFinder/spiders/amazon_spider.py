import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

def formatLink(url):
    pieces = url.split('/')
    # erl = ''
    for i, piece in enumerate(pieces):
        print i
        if piece == 'dp':
            erl = "https://www.amazon.com/dp/" + pieces[i+1][:10] + '/'
            print erl
            return erl
    return erl


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains= ['amazon.com']
    rules = [
        Rule(
            LinkExtractor(
                allow='/dp/',
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse"
        )
    ]

    def start_requests(self):
        urls = [
            'https://www.amazon.com/dp/B005FDOGCK/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        title = response.css("title")

        print "\n\nTitle:\n" + str(title) + "\n\n"
        links = LinkExtractor(allow='/dp/', canonicalize=True, unique=True).extract_links(response)

        for link in links:
            # print link.url
            yield scrapy.Request(url= formatLink(link.url), callback=self.parse)
