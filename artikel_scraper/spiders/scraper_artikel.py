# -*- coding: utf-8 -*-
# modified by harifrahman999@gmail.com

import scrapy

domain_identity = None

class ScraperArtikelSpider(scrapy.Spider):
    name = 'scraper_artikel'
    allowed_domains = ['travel.detik.com', 'viva.co.id', 'news.detik.com']
    
    global domain_identity
    url = input("masukkan url")

    start_urls = [url]
    # start_urls = ['https://news.detik.com/berita/d-4980111/hasil-rapid-test-negatif-161-jemaah-tablig-di-gorontalo-dipulangkan/']
    
    #simple checker for allowed domain
    for domain in allowed_domains:
        print(domain)
        if domain in url:
            print("allowed domain = ", domain)
            domain_identity = domain
    
    if domain_identity is None:
        print("==========% Site u want to access is not defined %========== ")
        exit()
    
    custom_settings={ 'FEED_URI': "scraper_artikel%(time)s.json",
                       'FEED_FORMAT': 'json'}

    def parse(self, response):
        # use this below to debug domain identity yg d kenal
        # print("\n\nini nama domain nya lek ------->", domain_identity)
        if domain_identity == 'news.detik.com':
            print("procesing:"+response.url)
            SET_SELECTOR = '.detail'
            for artikel in response.css(SET_SELECTOR):
                # pass
                JUDUL_SELECTOR = 'h1 ::text'
                IMAGE_SELECTOR = 'img ::attr(src)'
                DETAIL_BODY_SELECTOR = 'p ::text'
                scraped_info =  {
                    'name': artikel.css(JUDUL_SELECTOR).extract_first(),
                    'image': artikel.css(IMAGE_SELECTOR).extract_first(),
                    'content': artikel.css(DETAIL_BODY_SELECTOR).extract(),
                }

                yield scraped_info
        
        # masukin klo domain nya itu yg lain maka, lakukan crawl lain dengan slector sesuai domain
        # misal if domain_identity == 'viva.co.id': , tinggal set aja selector nya 