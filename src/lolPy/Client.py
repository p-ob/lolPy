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
from src.riot.Constants import *
from src.riot import *
from src.riot.Constants.RiotException import RiotException

DEBUG = True


class Client(object):
    """
    Client opens up connections between Python and RiotGames' API for League of Legends. It maps Json Objects from Riot
    into custom Python classes for easier management and use.
    """
    def __init__(self, username, region: str, api_key: str):
        self.__check_api_key(api_key)
        self.__name = username
        self.__region = region
        self.__key = api_key
        self.__player = None
        self.__search_for_player()

    def __check_api_key(self, api_key):
        payload = {"api_key": api_key}
        url = (urls.base + urls.player_by_name).format(region='na', summonerNames='drunk7irishman')
        r = requests.get(url, params=payload)
        if r.status_code == RiotException.AccessDenied:
            raise Exception("Api key is not recognized by RiotGames.")
        if r.status_code == RiotException.RateLimitExceeded:
            time.sleep(1)
            self.__check_api_key(api_key)

    @staticmethod
    def __api_service_check(request):
        if request.status_code != RiotException.NoException:
            if DEBUG:
                raise Exception('{0}: {1}'.format(request.status_code, request.reason))
            return False
        return True

    def __search_for_player(self):
        payload = {"api_key": self.__key}
        url = (urls.base + urls.player_by_name).format(region=self.__region, summonerNames=self.__name)
        r = requests.get(url, params=payload)
        if r.status_code == RiotException.NotFound:
            raise Exception("Player {0} not found in region {1}", self.__name, self.__region)
        if r.status_code == RiotException.RateLimitExceeded:
            time.sleep(1)
            self.__search_for_player()
        if not self.__api_service_check(r):
            self.__player = None
            return

        data = r.json()
        player = Player.Player(data[self.__name])
        self.__player = player

    def change_search_parameters(self, username=None, region: str=None):
        changed_region = False
        if region and region != self.__region:
            self.__region = region
            changed_region = True
        if username and (username != self.__name or changed_region):
            self.__name = username
            self.__search_for_player()

    def ranked_match_history(self, skip: int=0, include_timeline: bool=True):
        payload = {"api_key": self.__key, "beginIndex": skip}
        url = (urls.base + urls.ranked_match_history).format(region=self.__region, summonerId=self.__player.id)
        r = requests.get(url, params=payload)
        if r.status_code == RiotException.RateLimitExceeded:
            time.sleep(1)
            return self.ranked_match_history()
        if not self.__api_service_check(r):
            return []

        data = r.json()

        matches_json = data["matches"]

        matches = []
        for match in matches_json:
            match_id = match["matchId"]
            matches += [Match.Match(match_id, self.__match_details(match_id, include_timeline))]

        return matches

    def __match_details(self, match_id: int, include_timeline):
        payload = {"api_key": self.__key, "includeTimeline": include_timeline}
        url = (urls.base + urls.match_details).format(region=self.__region, matchId=match_id)
        r = requests.get(url, params=payload)
        if r.status_code == RiotException.RateLimitExceeded:
            time.sleep(1)
            return self.__match_details(match_id, include_timeline)
        if not self.__api_service_check(r):
            return []

        data = r.json()
        return data

    def recent_match_history(self, include_timeline: bool=False):
        payload = {"api_key": self.__key}
        url = (urls.base + urls.recent_match_history).format(region=self.__region, summonerId=self.__player.id)
        r = requests.get(url, params=payload)
        if r.status_code == RiotException.RateLimitExceeded:
            time.sleep(1)
            return self.recent_match_history()
        if not self.__api_service_check(r):
            return []

        data = r.json()

        matches_json = data["games"]

        matches = []
        for match in matches_json:
            match_id = match["gameId"]
            matches += [Match.Match(match_id, self.__match_details(match_id, include_timeline))]
        return matches