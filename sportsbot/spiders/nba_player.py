import scrapy
from sportsbot.items import NbaPlayerItem

class NbaPlayerSpider(scrapy.Spider):
    name = 'nba_player'

    start_urls = [
        'https://www.basketball-reference.com/players/e/edwaran01/gamelog/2025/'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="pgl_basic"]/tbody/tr'):
            player_item = NbaPlayerItem()
            
            player_item['date'] = row.xpath('.//td[@data-stat="date_game"]/a/text()').get()
            player_item['age'] = row.xpath('.//td[@data-stat="age"]/text()').get()
            player_item['team'] = row.xpath('.//td[@data-stat="team_id"]/a/text()').get()
            player_item['home_away'] = row.xpath('.//td[@data-stat="game_location"]/text()').get()
            player_item['opponent'] = row.xpath('.//td[@data-stat="opp_id"]/a/text()').get()
            player_item['result'] = row.xpath('.//td[@data-stat="game_result"]/text()').get()
            player_item['minutes'] = row.xpath('.//td[@data-stat="mp"]/text()').get()
            player_item['fg'] = row.xpath('.//td[@data-stat="fg"]/text()').get()
            player_item['fga'] = row.xpath('.//td[@data-stat="fga"]/text()').get()
            player_item['fg_percent'] = row.xpath('.//td[@data-stat="fg_pct"]/text()').get()
            player_item['threes'] = row.xpath('.//td[@data-stat="fg3"]/text()').get()
            player_item['threes_attempts'] = row.xpath('.//td[@data-stat="fg3a"]/text()').get()
            player_item['threes_percent'] = row.xpath('.//td[@data-stat="fg3_pct"]/text()').get()
            player_item['ft'] = row.xpath('.//td[@data-stat="ft"]/text()').get()
            player_item['fta'] = row.xpath('.//td[@data-stat="fta"]/text()').get()
            player_item['ft_percent'] = row.xpath('.//td[@data-stat="ft_pct"]/text()').get()
            player_item['orb'] = row.xpath('.//td[@data-stat="orb"]/text()').get()
            player_item['drb'] = row.xpath('.//td[@data-stat="drb"]/text()').get()
            player_item['trb'] = row.xpath('.//td[@data-stat="trb"]/text()').get()
            player_item['ast'] = row.xpath('.//td[@data-stat="ast"]/text()').get()
            player_item['stl'] = row.xpath('.//td[@data-stat="stl"]/text()').get()
            player_item['blk'] = row.xpath('.//td[@data-stat="blk"]/text()').get()
            player_item['tov'] = row.xpath('.//td[@data-stat="tov"]/text()').get()
            player_item['pf'] = row.xpath('.//td[@data-stat="pf"]/text()').get()
            player_item['pts'] = row.xpath('.//td[@data-stat="pts"]/text()').get()
            player_item['plus_minus'] = row.xpath('.//td[@data-stat="plus_minus"]/text()').get()
            
            yield player_item