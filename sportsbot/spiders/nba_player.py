import scrapy

class NbaPlayerSpider(scrapy.Spider):
    name = 'nba_player'

    start_urls = [
        'https://www.basketball-reference.com/players/e/edwaran01/gamelog/2025/'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="pgl_basic"]/tbody/tr'):
            yield {
                'Date': row.xpath('.//td[@data-stat="date_game"]/a/text()').get(),
                'Age': row.xpath('.//td[@data-stat="age"]/text()').get(),
                'Team': row.xpath('.//td[@data-stat="team_id"]/a/text()').get(),
                'Home/Away': row.xpath('.//td[@data-stat="game_location"]/text()').get(),
                'Opponent': row.xpath('.//td[@data-stat="opp_id"]/a/text()').get(),
                'Result': row.xpath('.//td[@data-stat="game_result"]/text()').get(),
                'Minutes': row.xpath('.//td[@data-stat="mp"]/text()').get(),
                'FG': row.xpath('.//td[@data-stat="fg"]/text()').get(),
                'FGA': row.xpath('.//td[@data-stat="fga"]/text()').get(),
                'FG%': row.xpath('.//td[@data-stat="fg_pct"]/text()').get(),
                '3P': row.xpath('.//td[@data-stat="fg3"]/text()').get(),
                '3PA': row.xpath('.//td[@data-stat="fg3a"]/text()').get(),
                '3P%': row.xpath('.//td[@data-stat="fg3_pct"]/text()').get(),
                'FT': row.xpath('.//td[@data-stat="ft"]/text()').get(),
                'FTA': row.xpath('.//td[@data-stat="fta"]/text()').get(),
                'FT%': row.xpath('.//td[@data-stat="ft_pct"]/text()').get(),
                'ORB': row.xpath('.//td[@data-stat="orb"]/text()').get(),
                'DRB': row.xpath('.//td[@data-stat="drb"]/text()').get(),
                'TRB': row.xpath('.//td[@data-stat="trb"]/text()').get(),
                'AST': row.xpath('.//td[@data-stat="ast"]/text()').get(),
                'STL': row.xpath('.//td[@data-stat="stl"]/text()').get(),
                'BLK': row.xpath('.//td[@data-stat="blk"]/text()').get(),
                'TOV': row.xpath('.//td[@data-stat="tov"]/text()').get(),
                'PF': row.xpath('.//td[@data-stat="pf"]/text()').get(),
                'PTS': row.xpath('.//td[@data-stat="pts"]/text()').get(),
                '+/-': row.xpath('.//td[@data-stat="plus_minus"]/text()').get(),
            }