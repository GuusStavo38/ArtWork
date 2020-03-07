from typing import Any, Dict

from crunch_etl import BaseScraper
from crunch_etl.base import TDictRecords

from crunch_etl import scrape_pipeline
from crunch_etl.loaders.json import JsonLoader


class ArtScraper(BaseScraper):
    def extract_resource(self, response_body: str, record: Dict[str, Any]) -> TDictRecords:
        results = self.parse_json(response_body)
        return [results]


scrape_pipeline(
    pipeline_name='scrape_auctions_list',
    description='Scrape the list of available auctions',
    scraper=ArtScraper(
        url='https://www.catawiki.nl/buyer/api/v1/auctions'
    ),
    loader_success=JsonLoader(
        filename='/home/guus/GIT/HOB/ArtWork/data/success/auctions',
        # conn_id='gcs'
    ),
    loader_fail=JsonLoader(
        filename='/home/guus/GIT/HOB/ArtWork/data/fail/auctions',
        # conn_id='gcs'
    )
)
