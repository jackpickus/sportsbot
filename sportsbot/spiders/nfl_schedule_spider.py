import scrapy

class NflScheduleSpider(scrapy.Spider):
    name = 'nfl_schedule'

    start_urls = [
        'https://www.pro-football-reference.com/teams/buf/2024.htm'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="games"]/tbody/tr'):
            yield {
                'Week Num': row.xpath('.//th[@data-stat="week_num"]/text()').get(),
                'Day': row.xpath('.//td[@data-stat="game_day_of_week"]/text()').get(),
                'Date': row.xpath('.//td[@data-stat="game_date"]/text()').get(),
                'Time': row.xpath('.//td[@data-stat="game_time"]/text()').get(),
                'Outcome': row.xpath('.//td[@data-stat="game_outcome"]/text()').get(),
                'OT': row.xpath('.//td[@data-stat="overtime"]/text()').get(),
                'Game Location': row.xpath('.//td[@data-stat="game_location"]/text()').get(),
                'Opponent': row.xpath('.//td[@data-stat="opp"]/a/text()').get(),
                'Team Points': row.xpath('.//td[@data-stat="pts_off"]/text()').get(),
                'Opp Points': row.xpath('.//td[@data-stat="pts_def"]/text()').get(),
                '1st Downs': row.xpath('.//td[@data-stat="first_down_off"]/text()').get(),
                'Total yards': row.xpath('.//td[@data-stat="first_off"]/text()').get(), 
                'PassY': row.xpath('.//td[@data-stat="pass_yds_off"]/text()').get(), 
                'RushY': row.xpath('.//td[@data-stat="rush_yds_off"]/text()').get(), 
                'Turnovers': row.xpath('.//td[@data-stat="to_off"]/text()').get(),
                'Opp 1st Downs': row.xpath('.//td[@data-stat="first_down_def"]/text()').get(),
                'Opp Total yards': row.xpath('.//td[@data-stat="yards_def"]/text()').get(), 
                'Opp PassY': row.xpath('.//td[@data-stat="pass_yds_def"]/text()').get(), 
                'Opp RushY': row.xpath('.//td[@data-stat="rush_yds_def"]/text()').get(), 
                'Opp Turnovers': row.xpath('.//td[@data-stat="to_def"]/text()').get(),
            }