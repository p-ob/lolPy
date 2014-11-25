__author__ = 'Patrick O\'Brien'
''' COPYRIGHT 2014
    This file is part of lolPy.

    lolPy is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    lolPy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with lolPy.  If not, see <http://www.gnu.org/licenses/>.
'''
from restPy import *
import urls as urls


class RiotApiClient:
    def __init__(self, region, key):
        self.region = region.lower()
        self.key = key
        self.client = Client.Client(urls.base.format(region))
        self.summoner_id = -1
        self.summoner = None

    def change_region(self, region):
        """
        If changing region, be sure to call search again; summoner_id is region specific
        :param region: new region to search in
        """
        self.region = region.lower()

    def search(self, summoner_name):
        r = Request.Request(urls.player_by_name)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerNames', summoner_name)
        r.add_query_parameter('api_key', self.key)

        self.summoner = getattr(self.client.execute_with_return_struct(r), summoner_name)
        self.summoner_id = getattr(self.summoner, 'id', -1)
        return self.summoner

    def ranked_match_history(self):
        if self.summoner is None:
            raise Exception("Must search for summoner first")

        r = Request.Request(urls.ranked_match_history)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        return self.client.execute_with_return_struct(r)

    def recent_match_history(self):
        if self.summoner is None:
            raise Exception("Must search for summoner first")

        r = Request.Request(urls.recent_match_history)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        return self.client.execute_with_return_struct(r)

    def ranked_stats(self):
        if self.summoner is None:
            raise Exception("Must search for summoner first")

        r = Request.Request(urls.ranked_stats)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        return self.client.execute_with_return_struct(r)

    def summary_stats(self):
        if self.summoner is None:
            raise Exception("Must search for summoner first")

        r = Request.Request(urls.summary_stats)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        return self.client.execute_with_return_struct(r)

    def match_details(self, match_id, include_timeline: bool=True):
        r = Request.Request(urls.match_details)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('matchId', match_id)
        r.add_query_parameter('api_key', self.key)
        r.add_query_parameter('includeTimeline', include_timeline)

        return self.client.execute_with_return_struct(r)

    def champion_data(self):
        r = Request.Request(urls.champion_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        return self.client.execute_with_return_struct(r)