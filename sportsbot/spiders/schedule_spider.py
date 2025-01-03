import scrapy

class ScheduleSpider(scrapy.Spider):
    name = 'schedule'

    start_urls = [
        'https://www.sports-reference.com/cbb/schools/duke/men/2025-schedule.html'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="schedule"]/tbody/tr'):
            yield {
                'Date': row.xpath('//td[@data-stat="date_game"]/a/text()').getall(),
                'Time': row.xpath('//td[@data-stat="time_game"]/text()').getall(),
                'Opponent': row.xpath('//td[@data-stat="opp_name"]/a/text()').getall(),
                'Conference': row.xpath('//td[@data-stat="conf_abbr"]/a/text()').getall(),
                'SRS': row.xpath('//td[@data-stat="srs"]/text()').getall(),
                'Result': row.xpath('//td[@data-stat="game_result"]/text()').getall(),
                'Team Points': row.xpath('//td[@data-stat="pts"]/text()').getall(),
                'Opp Points': row.xpath('//td[@data-stat="opp_pts"]/text()').getall(),
                'OT': row.xpath('//td[@data-stat="overtimes"]/text()').getall(),
                'W': row.xpath('//td[@data-stat="wins"]/text()').getall(),
                'L': row.xpath('//td[@data-stat="losses"]/text()').getall(),
                'Streak': row.xpath('//td[@data-stat="game_streak"]/text()').getall(),
                'Arena': row.xpath('//td[@data-stat="arena"]/text()').getall()
            }