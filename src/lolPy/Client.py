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
import requests
import time
from src.lolApi.Constants import *
from src.lolApi import *

DEBUG = True


class Client(object):
    def __init__(self, username, region: str, api_key: str, rate_limit: int=10):
        self.name = username
        self.region = region
        self.key = api_key
        self.player = None
        self.rate_limit = rate_limit
        self.__search_for_player()

    @staticmethod
    def __api_service_check(request):
        if request.status_code != 200:
            if DEBUG:
                raise Exception('{0}: {1}'.format(request.status_code, request.reason))
            return False
        return True

    def __search_for_player(self):
        payload = {"api_key": self.key}
        url = (LolUrls.base + LolUrls.player_by_name).format(region=self.region, summonerNames=self.name)
        r = requests.get(url, params=payload)
        self.__api_service_check(r)

        data = r.json()
        player = Player.Player(data[self.name])
        self.player = player

    def ranked_match_history(self, skip: int=0, include_timeline: bool=True):
        payload = {"api_key": self.key, "beginIndex": skip}
        url = (LolUrls.base + LolUrls.ranked_match_history).format(region=self.region, summonerId=self.player.id)
        r = requests.get(url, params=payload)
        if r.status_code == 429:
            time.sleep(1)
            return self.ranked_match_history()
        if not self.__api_service_check(r):
            return {}

        data = r.json()

        matches_json = data["matches"]

        matches = []
        for match in matches_json:
            match_id = match["matchId"]
            matches += [Match.Match(match_id, self.__match_details(match_id, include_timeline))]

        return matches

    def __match_details(self, match_id: int, include_timeline):
        payload = {"api_key": self.key, "includeTimeline": include_timeline}
        url = (LolUrls.base + LolUrls.match_details).format(region=self.region, matchId=match_id)
        r = requests.get(url, params=payload)
        if r.status_code == 429:
            time.sleep(1)
            return self.__match_details(match_id, include_timeline)
        if not self.__api_service_check(r):
            return {}

        data = r.json()
        return data

    def recent_match_history(self, include_timeline: bool=False):
        payload = {"api_key": self.key}
        url = (LolUrls.base + LolUrls.recent_match_history).format(region=self.region, summonerId=self.player.id)
        r = requests.get(url, params=payload)
        if r.status_code == 429:
            time.sleep(1)
            return self.recent_match_history()
        if not self.__api_service_check(r):
            return {}

        data = r.json()

        matches_json = data["games"]

        matches = []
        for match in matches_json:
            match_id = match["gameId"]
            matches += [Match.Match(match_id, self.__match_details(match_id, include_timeline))]
        return matches
