import scrapy

class ScheduleSpider(scrapy.Spider):
    name = 'schedule'

    start_urls = [
        'https://www.sports-reference.com/cbb/schools/duke/men/2025-schedule.html'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="schedule"]/tbody'):
            yield {
                'Date': row.xpath('//tr/td[@data-stat="date_game"]/a/text()').getall(),
                'Time': row.xpath('//tr/td[@data-stat="time_game"]/text()').getall(),
                'Opponent': row.xpath('//tr/td[@data-stat="opp_name"]/a/text()').getall(),
                'Conference': row.xpath('//tr/td[@data-stat="conf_abbr"]/a/text()').getall(),
                'SRS': row.xpath('//tr/td[@data-stat="srs"]/text()').getall(),
                'Result': row.xpath('//tr/td[@data-stat="game_result"]/text()').getall(),
                'Team Points': row.xpath('//tr/td[@data-stat="pts"]/text()').getall(),
                'Opp Points': row.xpath('//tr/td[@data-stat="opp_pts"]/text()').getall(),
                'OT': row.xpath('//tr/td[@data-stat="overtimes"]/text()').getall(),
                'W': row.xpath('//tr/td[@data-stat="wins"]/text()').getall(),
                'L': row.xpath('//tr/td[@data-stat="losses"]/text()').getall(),
                'Streak': row.xpath('//tr/td[@data-stat="game_streak"]/text()').getall(),
                'Arena': row.xpath('//tr/td[@dtr/ata-stat="arena"]/text()').getall()
            }