import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

def formatLink(url):
    pieces = url.split('/')
    # erl = ''
    for i, piece in enumerate(pieces):
        if piece == 'dp':
            erl = "https://www.amazon.com/dp/" + pieces[i+1][:10] + '/'
            print erl
            return erl
        if piece == 'product':
            erl = "https://www.amazon.com/dp/" + pieces[i+1][:10] + '/'
            print erl
            return erl
    return ""


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


# //*[@id="pagnNextLink"]

    def start_requests(self):
        urls = [
            # 'https://www.amazon.com/s/rh=i%3Atoys-and-games%2Cn%3A165793011%2Cn%3A%21165795011%2Cn%3A165993011%2Cn%3A2514571011/ref=s9_acss_bw_ln_sgleft_1_1_w?_encoding=UTF8&bbn=165993011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=6QNZN902PMT84Z68YGWZ&pf_rd_r=6QNZN902PMT84Z68YGWZ&pf_rd_t=101&pf_rd_p=20ad8f7e-b71e-4012-b1fc-ef852c2b8022&pf_rd_p=20ad8f7e-b71e-4012-b1fc-ef852c2b8022&pf_rd_i=165793011'
            # 'https://www.amazon.com/dp/B005FDOGCK/'
            'https://www.amazon.com/s/rh=i%3Atoys-and-games%2Cn%3A165793011%2Cn%3A%21165795011%2Cn%3A165993011%2Cn%3A2514571011/ref=s9_acss_bw_ln_sgleft_1_1_w?_encoding=UTF8'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def getItemData(self, response):
        print '\n hello world \n'


    def parse(self, response):
        title = response.css("title")

        retUrl = "amazon.com" + response.css("#pagnNextLink::attr(href)").extract_first()
        print "\n\n\n"
        print retUrl
        print "\n\n\n\n\n"

        links = LinkExtractor(allow=['/dp/','/gp' ], canonicalize=True, unique=True).extract_links(response)

        for link in links:
            # print link.url
            uri = formatLink(link.url)
            print uri
            scrapy.Request(url= uri, callback=self.getItemData)

        return scrapy.Request(url= retUrl, callback=self.parse)
