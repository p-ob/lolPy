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
from lolPy import urls


class RiotApiClient:
    def __init__(self, key, region, return_json: bool=False):
        self.region = region.lower()
        self.key = key
        self.client = Client.Client(urls.base.format(self.region))
        self.summoner_id = -1
        self.summoner = None
        self.return_json = return_json

    def change_region(self, region):
        """
        If changing region, be sure to call search again; summoner_id is region specific
        :param region: new region to search in
        """
        self.region = region.lower()
        self.summoner = None
        self.summoner_id = -1
        self.client = Client.Client(urls.base.format(self.region))

    def search(self, summoner_names, return_json: bool=False):
        """
        :param summoner_names:
        :return:
        """
        if len(summoner_names) > 40:
            raise Exception("Too many summoners. Riot only allows up to 40.")
        elif len(summoner_names) < 1:
            raise Exception("Need at least one summoner!")
        r = Request.Request(urls.player_by_name)
        r.add_url_parameter('region', self.region)
        if isinstance(summoner_names, list) or isinstance(summoner_names, tuple):
            r.add_url_parameter('summonerNames', ','.join(summoner_names))
        elif isinstance(summoner_names, str):
            r.add_url_parameter('summonerNames', summoner_names)
        r.add_query_parameter('api_key', self.key)

        val = self.client.execute_with_return_struct(r)
        if isinstance(summoner_names, list) or isinstance(summoner_names, tuple):
            self.summoner = getattr(val, summoner_names[0].lower().replace(' ', ''), None)
        else:
            self.summoner = getattr(val, summoner_names.lower().replace(' ', ''))
        self.summoner_id = getattr(self.summoner, 'id', -1)
        if return_json or self.return_json:
            return self.client.execute(r).json()
        if isinstance(summoner_names, list) or isinstance(summoner_names, tuple):
            return [getattr(val, s.lower().replace(' ', '')) for s in summoner_names] if len(
                summoner_names) > 1 else self.summoner
        else:
            return getattr(val, summoner_names.lower().replace(' ', ''))

    def ranked_match_history(self, return_json: bool=False):
        if self.summoner is None:
            raise Exception("Must search for summoner first")

        r = Request.Request(urls.ranked_match_history)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def recent_match_history(self, return_json: bool=False):
        if self.summoner is None:
            raise Exception("Must search for summoner first")

        r = Request.Request(urls.recent_match_history)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def ranked_stats(self, return_json: bool=False):
        if self.summoner is None:
            raise Exception("Must search for summoner first")

        r = Request.Request(urls.ranked_stats)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def summary_stats(self, return_json: bool=False):
        if self.summoner is None:
            raise Exception("Must search for summoner first")

        r = Request.Request(urls.summary_stats)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def match_details(self, match_id, include_timeline: bool=True, return_json: bool=False):
        r = Request.Request(urls.match_details)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('matchId', match_id)
        r.add_query_parameter('api_key', self.key)
        r.add_query_parameter('includeTimeline', include_timeline)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def champion_data(self, champion_id: int=-1, return_json: bool=False):
        if champion_id >= 0:
            r = Request.Request(urls.champion_data_by_id)
            r.add_url_parameter('id', champion_id)
        else:
            r = Request.Request(urls.champion_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def rune_data(self, rune_id: int=-1, return_json: bool=False):
        if rune_id >= 0:
            r = Request.Request(urls.rune_data_by_id)
            r.add_url_parameter('id', rune_id)
        else:
            r = Request.Request(urls.rune_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def mastery_data(self, mastery_id: int=-1, return_json: bool=False):
        if mastery_id >= 0:
            r = Request.Request(urls.mastery_data_by_id)
            r.add_url_parameter('id', mastery_id)
        else:
            r = Request.Request(urls.mastery_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def item_data(self, item_id: int=-1, return_json: bool=False):
        if item_id >= 0:
            r = Request.Request(urls.item_data_by_id)
            r.add_url_parameter('id', item_id)
        else:
            r = Request.Request(urls.item_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def summoner_spell_data(self, summoner_spell_id: int=-1, return_json: bool=False):
        if summoner_spell_id >= 0:
            r = Request.Request(urls.summoner_spell_data_by_id)
            r.add_url_parameter('id', summoner_spell_id)
        else:
            r = Request.Request(urls.summoner_spell_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def league_data(self, return_json: bool=False):
        r = Request.Request(urls.league_data)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerIds', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self.return_json:
            return self.client.execute(r).json()
        return getattr(self.client.execute_with_return_struct(r), str(self.summoner_id))


