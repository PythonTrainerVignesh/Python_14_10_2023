from pathlib import Path
import csv

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        urls = [
            "https://www.amazon.in/s?k=mobiles",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-color-base", " " )) and '
                              'contains(concat( " ", @class, " " ), concat( " ", "a-text-normal", " " ))]/text('
                              ')').getall()
        with open('mobiles.csv', 'a', encoding="utf-8") as file:
            file.write('mobile names\n')
            for i in data:
                x = i.replace('"', '')
                file.write(f'"{x}"' + '\n')
