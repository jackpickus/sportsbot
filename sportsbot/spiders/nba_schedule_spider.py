import scrapy

class NbaScheduleSpider(scrapy.Spider):
    name = 'nba_schedule'

    start_urls = [
        'https://www.basketball-reference.com/teams/CHI/2025_games.html',
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="games"]/tbody/tr'):
            yield {
                'Date': row.xpath('.//td[@data-stat="date_game"]/a/text()').get(),
                'Time (ET)': row.xpath('.//td[@data-stat="game_start_time"]/text()').get(),
                'Home/Away': row.xpath('.//td[@data-stat="game_location"]/text()').get(),
                'Opponent': row.xpath('.//td[@data-stat="opp_name"]/a/text()').get(),
                'Result': row.xpath('.//td[@data-stat="game_result"]/text()').get(),
                'Team Points': row.xpath('.//td[@data-stat="pts"]/text()').get(),
                'Opp Points': row.xpath('.//td[@data-stat="opp_pts"]/text()').get(),
                'W': row.xpath('.//td[@data-stat="wins"]/text()').get(),
                'L': row.xpath('.//td[@data-stat="losses"]/text()').get(),
                'Streak': row.xpath('.//td[@data-stat="game_streak"]/text()').get(),
            }