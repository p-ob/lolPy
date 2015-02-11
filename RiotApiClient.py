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
from RegionId import RegionId
from PlatformId import PlatformId
from requests import HTTPError


class RiotApiException(Exception):
    pass


class RiotApiClient:
    def __init__(self, key: str, region: str, return_json: bool=False):
        """

        :param key: API key given by https://developer.riotgames.com
        :param region: Region for RiotApiClient to query (valid strings are in Region.py)
        :param return_json: bool that tells RiotApiClient to return the raw json object (note that summoner_id will need
            to be set manually
        :return: RiotApiClient, with default (and invalid) attribute values
        """
        self.region = region.lower()
        self.key = key
        self.client = Client.Client(urls.base.format(self.region))
        self._current_summoner_index = 0
        self.summoners = []
        self._return_json = return_json

    def _match_region_to_platform(self):
        if self.region == RegionId.na:
            return PlatformId.na1
        if self.region == RegionId.br:
            return PlatformId.br1
        if self.region == RegionId.eune:
            return PlatformId.eun1
        if self.region == RegionId.euw:
            return PlatformId.euw1
        if self.region == RegionId.kr:
            return PlatformId.kr
        if self.region == RegionId.oce:
            return PlatformId.oc1
        if self.region == RegionId.tr:
            return PlatformId.tr1
        if self.region == RegionId.lan:
            return PlatformId.la1
        if self.region == RegionId.las:
            return PlatformId.la2
        if self.region == RegionId.ru:
            return PlatformId.ru

    def change_region(self, region: str):
        """
        If changing region, be sure to call search again; summoner_id is region specific
        :param region: new region to search in
        """
        self.region = region.lower()
        self.summoners = []
        self.client = Client.Client(urls.base.format(self.region))
        self._current_summoner_index = 0

    def next(self) -> Client.Struct:
        """
        updates self.summoner_id to the id of the next summoner
        :return: Struct representing the next summoner
        """
        assert isinstance(self.summoners, list)
        if self.summoners is []:
            raise RiotApiException('RiotApiClient.summoners is not populated; cannot get next summoner.')

        self._current_summoner_index += 1
        return self.current_summoner

    @property
    def current_summoner(self) -> Client.Struct:
        """
        uses the index of the current summoner to retrieve the summoner Struct
        :return: Struct representing a summoner
        """
        assert isinstance(self.summoners, list)
        return self.summoners[self._current_summoner_index % len(self.summoners)]

    @property
    def summoner_id(self):
        return self.current_summoner.id

    def search(self, summoner_names, return_json: bool=False) -> Client.Struct:
        """
        populates self.summoners with a list of Structs, each Struct representing a summoner
        :param summoner_names: list of strings or single string representing the summoner names to be searched
        :param return_json: bool that when set to True returns the raw jason object
        :return: the first summoner stored in self.summoners list (e.g. the first summoner in summoner_names)
        """
        if not (isinstance(summoner_names, list) or isinstance(summoner_names, tuple)):
            summoner_names = [summoner_names]
        if len(summoner_names) > 40:
            raise RiotApiException("Too many summoners. Riot only allows up to 40.")
        elif len(summoner_names) < 1:
            raise RiotApiException("Need at least one summoner.")
        r = Request.Request(urls.player_by_name)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerNames', ','.join(summoner_names))
        r.add_query_parameter('api_key', self.key)

        search_results = self.client.execute_with_return_struct(r)
        self.summoners = [getattr(search_results, s.lower().replace(' ', '')) for s in summoner_names]
        self._current_summoner_index = 0
        if return_json or self._return_json:
            return self.client.execute(r).json()
        return self.summoners[0]

    def ranked_match_history(self, return_json: bool=False) -> list:
        """

        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if self.summoner_id < 0:
            raise RiotApiException("RiotApiClient.summoner_id is invalid")

        r = Request.Request(urls.ranked_match_history)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        return getattr(self.client.execute_with_return_struct(r), 'matches', [])

    def recent_match_history(self, return_json: bool=False) -> list:
        """

        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if self.summoner_id < 0:
            raise RiotApiException("RiotApiClient.summoner_id is invalid")

        r = Request.Request(urls.recent_match_history)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        return getattr(self.client.execute_with_return_struct(r), 'games', [])

    def ranked_stats(self, return_json: bool=False) -> Client.Struct:
        """

        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if self.summoner_id < 0:
            raise RiotApiException("RiotApiClient.summoner_id is invalid")

        r = Request.Request(urls.ranked_stats)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def summary_stats(self, return_json: bool=False) -> Client.Struct:
        """

        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if self.summoner_id < 0:
            raise RiotApiException("RiotApiClient.summoner_id is invalid")

        r = Request.Request(urls.summary_stats)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def match_details(self, match_id, include_timeline: bool=True, return_json: bool=False) -> Client.Struct:
        """

        :param match_id:
        :param include_timeline:
        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        r = Request.Request(urls.match_details)
        r.add_url_parameter('region', self.region)
        r.add_url_parameter('matchId', match_id)
        r.add_query_parameter('api_key', self.key)
        r.add_query_parameter('includeTimeline', include_timeline)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        return self.client.execute_with_return_struct(r)

    def champion_data(self, champion_id: int=-1, return_json: bool=False) -> Client.Struct:
        """

        :param champion_id:
        :param return_json: bool that when set to True returns the raw jason object
        :return: if champion_id is given, returns a Struct; otherwise, a list of Structs; these Structs are each
            champion data type object
        """
        if champion_id >= 0:
            r = Request.Request(urls.champion_data_by_id)
            r.add_url_parameter('id', champion_id)
        else:
            r = Request.Request(urls.champion_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        if champion_id < 0:
            return getattr(self.client.execute_with_return_struct(r), 'data')
        return self.client.execute_with_return_struct(r)

    def rune_data(self, rune_id: int=-1, return_json: bool=False) -> Client.Struct:
        """

        :param rune_id:
        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if rune_id >= 0:
            r = Request.Request(urls.rune_data_by_id)
            r.add_url_parameter('id', rune_id)
        else:
            r = Request.Request(urls.rune_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        if rune_id < 0:
            return getattr(self.client.execute_with_return_struct(r), 'data')
        return self.client.execute_with_return_struct(r)

    def mastery_data(self, mastery_id: int=-1, return_json: bool=False) -> Client.Struct:
        """

        :param mastery_id:
        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if mastery_id >= 0:
            r = Request.Request(urls.mastery_data_by_id)
            r.add_url_parameter('id', mastery_id)
        else:
            r = Request.Request(urls.mastery_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        if mastery_id < 0:
            return getattr(self.client.execute_with_return_struct(r), 'data')
        return self.client.execute_with_return_struct(r)

    def item_data(self, item_id: int=-1, item_list_data: str='', return_json: bool=False) -> Client.Struct:
        """

        :param item_id:
        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if item_id >= 0:
            r = Request.Request(urls.item_data_by_id)
            r.add_url_parameter('id', item_id)
        else:
            r = Request.Request(urls.item_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)
        if item_list_data:
            r.add_query_parameter('itemListData', item_list_data)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        if item_id < 0:
            return getattr(self.client.execute_with_return_struct(r), 'data')
        return self.client.execute_with_return_struct(r)

    def summoner_spell_data(self, summoner_spell_id: int=-1, return_json: bool=False) -> Client.Struct:
        """

        :param summoner_spell_id:
        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if summoner_spell_id >= 0:
            r = Request.Request(urls.summoner_spell_data_by_id)
            r.add_url_parameter('id', summoner_spell_id)
        else:
            r = Request.Request(urls.summoner_spell_data)
        r.add_url_parameter('region', self.region)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        if summoner_spell_id < 0:
            return getattr(self.client.execute_with_return_struct(r), 'data')
        return self.client.execute_with_return_struct(r)

    def league_data(self, all_summoners: bool=False, return_json: bool=False) -> Client.Struct:
        """

        :param return_json: bool that when set to True returns the raw jason object
        :return:
        """
        if self.summoner_id < 0:
            raise RiotApiException("RiotApiClient.summoner_id is invalid")

        r = Request.Request(urls.league_data)
        r.add_url_parameter('region', self.region)
        rest_summoners = []
        if all_summoners:
            current_summoners = self.summoners
            if len(self.summoners) > 10:
                current_summoners = self.summoners[:10]
                rest_summoners = self.summoners[10:]
            summoner_ids = [str(summoner.id) for summoner in current_summoners]
            r.add_url_parameter('summonerIds', ','.join(summoner_ids))
        else:
            summoner_ids = []
            r.add_url_parameter('summonerIds', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()

        if all_summoners and summoner_ids:
            all_league_data = self.client.execute_with_return_struct(r)
            all_league_data = [getattr(all_league_data, summoner_id, None) for summoner_id in summoner_ids]
            return_data = []
            for i in range(len(all_league_data)):
                this_summoner_id = summoner_ids[i]
                if not all_league_data[i]:
                    continue
                for this_league_data in all_league_data[i]:
                    setattr(this_league_data, 'summonerId', this_summoner_id)
                    return_data += [this_league_data]
            if len(self.summoners) > 10:
                temp_client = RiotApiClient(self.key, self.region)
                temp_client.summoners = rest_summoners
                return_data += temp_client.league_data(all_summoners=True)
            return return_data

        return getattr(self.client.execute_with_return_struct(r), str(self.summoner_id))

    def current_game_data(self, return_json: bool=False) -> Client.Struct:
        if self.summoner_id < 0:
            raise RiotApiException("RiotApiClient.summoner_id is invalid")

        r = Request.Request(urls.current_game)
        r.add_url_parameter('platformId', self._match_region_to_platform())
        r.add_url_parameter('summonerId', self.summoner_id)
        r.add_query_parameter('api_key', self.key)

        if return_json or self._return_json:
            return self.client.execute(r).json()
        try:
            return self.client.execute_with_return_struct(r)
        except HTTPError as e:
            # if an HTTPError is thrown with code 404, then they're not in a game
            if e.response.status_code == 404:
                return None
            raise e



