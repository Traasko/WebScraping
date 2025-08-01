import scrapy
from recettes_scrapy.items import RecetteItem

class RecettesSpider(scrapy.Spider):
    name = "recettes_spider"
    allowed_domains = ["cuisineaz.com"]
    start_urls = [
        'https://www.cuisineaz.com/recettes/crepe-facile-78347.aspx',
        'https://www.cuisineaz.com/recettes/courgettes-farcies-legeres-54220.aspx',
        'https://www.cuisineaz.com/recettes/lasagnes-a-la-bolognaise-facile-54832.aspx',
        'https://www.cuisineaz.com/recettes/gratin-de-pates-au-fromage-de-chevre-7659.aspx'
    ]

    def parse(self, response):
        item = RecetteItem()

        item['titre'] = response.css('.recipe-title::text').get(default='').strip()

        ingredients = response.css('.ingredient_label::text').getall()
        item['ingredients'] = [ing.strip() for ing in ingredients if ing.strip()]

        temps = response.css('.recipe_time_information::text').getall()
        temps = [t.strip() for t in temps if t.strip()]
        item['temps_preparation'] = " ".join(temps) if temps else ''

        etapes = response.css('.preparation_step_title_container > h3.recipe_section_h3::text').getall()
        item['etapes'] = [etape.strip() for etape in etapes if etape.strip()]

        yield item
