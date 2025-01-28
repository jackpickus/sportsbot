import scrapy


class SportsbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def serialize_home_away(value):
    if value == '@':
        return 'A'
    else:
        return 'H'

class NbaPlayerItem(scrapy.Item):
    date = scrapy.Field()
    age = scrapy.Field()
    team = scrapy.Field()
    home_away = scrapy.Field(serializer=serialize_home_away)
    opponent = scrapy.Field()
    result = scrapy.Field()
    minutes = scrapy.Field()
    fg = scrapy.Field()
    fga = scrapy.Field()
    fg_percent = scrapy.Field()
    threes = scrapy.Field()
    threes_attempts = scrapy.Field()
    threes_percent = scrapy.Field()
    ft = scrapy.Field()
    fta = scrapy.Field()
    ft_percent = scrapy.Field()
    orb = scrapy.Field()
    drb = scrapy.Field()
    trb = scrapy.Field()
    ast = scrapy.Field()
    stl = scrapy.Field()
    blk = scrapy.Field()
    tov = scrapy.Field()
    pf = scrapy.Field()
    pts = scrapy.Field()
    plus_minus = scrapy.Field()
