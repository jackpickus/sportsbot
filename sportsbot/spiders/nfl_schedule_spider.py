import scrapy

class NflScheduleSpider(scrapy.Spider):
    name = 'nfl_schedule'

    start_urls = [
        'https://www.pro-football-reference.com/teams/buf/2024.htm'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="games"]/tbody/tr'):
            yield {
                'Week Num': row.xpath('.//th[@data-stat="week_num"]/text()').extract_first(),
                'Day': row.xpath('.//td[@data-stat="game_day_of_week"]/text()').extract_first(),
                'Date': row.xpath('.//td[@data-stat="game_date"]/text()').extract_first(),
                'Time': row.xpath('.//td[@data-stat="game_time"]/text()').extract_first(),
                'Outcome': row.xpath('.//td[@data-stat="game_outcome"]/text()').extract_first(),
                'OT': row.xpath('.//td[@data-stat="overtime"]/text()').extract_first(),
                'Game Location': row.xpath('.//td[@data-stat="game_location"]/text()').extract_first(),
                'Opponent': row.xpath('.//td[@data-stat="opp"]/a/text()').extract_first(),
                'Team Points': row.xpath('.//td[@data-stat="pts_off"]/text()').extract_first(),
                'Opp Points': row.xpath('.//td[@data-stat="pts_def"]/text()').extract_first(),
                '1st Downs': row.xpath('.//td[@data-stat="first_down_off"]/text()').extract_first(),
                'Total yards': row.xpath('.//td[@data-stat="first_off"]/text()').extract_first(), 
                'PassY': row.xpath('.//td[@data-stat="pass_yds_off"]/text()').extract_first(), 
                'RushY': row.xpath('.//td[@data-stat="rush_yds_off"]/text()').extract_first(), 
                'Turnovers': row.xpath('.//td[@data-stat="to_off"]/text()').extract_first(),
                'Opp 1st Downs': row.xpath('.//td[@data-stat="first_down_def"]/text()').extract_first(),
                'Opp Total yards': row.xpath('.//td[@data-stat="yards_def"]/text()').extract_first(), 
                'Opp PassY': row.xpath('.//td[@data-stat="pass_yds_def"]/text()').extract_first(), 
                'Opp RushY': row.xpath('.//td[@data-stat="rush_yds_def"]/text()').extract_first(), 
                'Opp Turnovers': row.xpath('.//td[@data-stat="to_def"]/text()').extract_first(),
            }