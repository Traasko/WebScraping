import scrapy

class RecetteItem(scrapy.Item):
    titre = scrapy.Field()
    ingredients = scrapy.Field()
    etapes = scrapy.Field()
    temps_preparation = scrapy.Field()
