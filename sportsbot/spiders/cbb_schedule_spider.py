import scrapy

class CbbScheduleSpider(scrapy.Spider):
    name = 'cbb_schedule'

    start_urls = [
        'https://www.sports-reference.com/cbb/schools/duke/men/2025-schedule.html'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="schedule"]/tbody/tr'):
            yield {
                'Date': row.xpath('.//td[@data-stat="date_game"]/a/text()').get(),
                'Time': row.xpath('.//td[@data-stat="time_game"]/text()').get(),
                'Opponent': row.xpath('.//td[@data-stat="opp_name"]/a/text()').get(),
                'Conference': row.xpath('.//td[@data-stat="conf_abbr"]/a/text()').get(),
                'SRS': row.xpath('.//td[@data-stat="srs"]/text()').get(),
                'Result': row.xpath('.//td[@data-stat="game_result"]/text()').get(),
                'Team Points': row.xpath('.//td[@data-stat="pts"]/text()').get(),
                'Opp Points': row.xpath('.//td[@data-stat="opp_pts"]/text()').get(),
                'OT': row.xpath('.//td[@data-stat="overtimes"]/text()').get(),
                'W': row.xpath('.//td[@data-stat="wins"]/text()').get(),
                'L': row.xpath('.//td[@data-stat="losses"]/text()').get(),
                'Streak': row.xpath('.//td[@data-stat="game_streak"]/text()').get(),
                'Arena': row.xpath('.//td[@data-stat="arena"]/text()').get()
            }