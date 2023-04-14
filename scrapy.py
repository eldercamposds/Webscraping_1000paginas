import scrapy


class JogosSpider(scrapy.Spider):
    name = "jogos"
    start_urls = ["https://boardgamegeek.com/browse/boardgame/page/1"]

    def parse(self, response):
        for jogo in response.css('#row_'):
            yield {
            'rank' : jogo.css('.collection_rank a::attr(name)').get(),
            'nome' : jogo.css('.primary ::text').get(),  
            'avaliacao' : jogo.css('#row_ .collection_bggrating:nth-child(5)').get().split()[3]
            }

        #navegando pelas paginas
        prox_pag = response.xpath('//*[@id="maincontent"]/form/div/div[1]/a[5]').attrib['href']
        
        if prox_pag is not None:
            # caso a proxima pagina não esteva vazia
            yield response.follow(prox_pag, callback=self.parse)
