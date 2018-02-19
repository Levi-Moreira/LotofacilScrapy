import scrapy
from scrapy.loader import ItemLoader

from lottery.items import LotteryItem


class LotoFacilSpider(scrapy.Spider):
    name = "lotofacil"
    initial_lottery_number = 1625
    # end_lottery_number = 1628

    def start_requests(self):
        url = 'https://www.sorteonline.com.br/lotofacil/resultados'
        for i in range(self.initial_lottery_number, 1, -1):
            formData = {"numeroConcurso": str(i)}
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=formData)

    def parse(self, response):
        loader = ItemLoader(item=LotteryItem(), response=response)
        loader.add_xpath('lottery_number',
                         '//h3[@class="col text align-center no-mobile color"][2]/span[@class="bold"]/text()')

        loader.add_xpath('lottery_date',
                         '//h3[@class="col text align-center no-mobile color"][1]/span[@class="bold"]/text()')

        loader.add_xpath('lottery_result_numbers', '//div[@class="block-result color"]//*[@class="bg"]/text()')

        loader.add_xpath('lottery_15_winners', '//div[@class="block-table"]/table[@class="result"]/tr[2]/td[2]/text()')
        loader.add_xpath('lottery_15_winners_cash',
                         '//div[@class="block-table"]/table[@class="result"]/tr[2]/td[3]/text()')
        loader.add_xpath('lottery_14_winners', '//div[@class="block-table"]/table[@class="result"]/tr[3]/td[2]/text()')
        loader.add_xpath('lottery_14_winners_cash',
                         '//div[@class="block-table"]/table[@class="result"]/tr[3]/td[3]/text()')
        loader.add_xpath('lottery_13_winners', '//div[@class="block-table"]/table[@class="result"]/tr[4]/td[2]/text()')
        loader.add_xpath('lottery_13_winners_cash',
                         '//div[@class="block-table"]/table[@class="result"]/tr[4]/td[3]/text()')
        loader.add_xpath('lottery_12_winners', '//div[@class="block-table"]/table[@class="result"]/tr[5]/td[2]/text()')
        loader.add_xpath('lottery_12_winners_cash',
                         '//div[@class="block-table"]/table[@class="result"]/tr[5]/td[3]/text()')
        loader.add_xpath('lottery_11_winners', '//div[@class="block-table"]/table[@class="result"]/tr[6]/td[2]/text()')
        loader.add_xpath('lottery_11_winners_cash',
                         '//div[@class="block-table"]/table[@class="result"]/tr[6]/td[3]/text()')

        return loader.load_item()
