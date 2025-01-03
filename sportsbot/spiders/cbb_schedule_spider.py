import scrapy

class CbbScheduleSpider(scrapy.Spider):
    name = 'cbb_schedule'

    start_urls = [
        'https://www.sports-reference.com/cbb/schools/duke/men/2025-schedule.html'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@id="schedule"]/tbody/tr'):
            yield {
                'Date': row.xpath('.//td[@data-stat="date_game"]/a/text()').extract_first(),
                'Time': row.xpath('.//td[@data-stat="time_game"]/text()').extract_first(),
                'Opponent': row.xpath('.//td[@data-stat="opp_name"]/a/text()').extract_first(),
                'Conference': row.xpath('.//td[@data-stat="conf_abbr"]/a/text()').extract_first(),
                'SRS': row.xpath('.//td[@data-stat="srs"]/text()').extract_first(),
                'Result': row.xpath('.//td[@data-stat="game_result"]/text()').extract_first(),
                'Team Points': row.xpath('.//td[@data-stat="pts"]/text()').extract_first(),
                'Opp Points': row.xpath('.//td[@data-stat="opp_pts"]/text()').extract_first(),
                'OT': row.xpath('.//td[@data-stat="overtimes"]/text()').extract_first(),
                'W': row.xpath('.//td[@data-stat="wins"]/text()').extract_first(),
                'L': row.xpath('.//td[@data-stat="losses"]/text()').extract_first(),
                'Streak': row.xpath('.//td[@data-stat="game_streak"]/text()').extract_first(),
                'Arena': row.xpath('.//td[@data-stat="arena"]/text()').extract_first()
            }