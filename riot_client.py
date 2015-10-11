__author__ = 'Patrick O\'Brien'
''' COPYRIGHT 2015
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

from typing import Any, List
import requests
import time


URLS = dict(
    summoner_by_name='v1.4/summoner/by-name/{summonerName}',
    summoner_by_id='v1.4/summoner/{summonerId}',
    match_list='v2.2/matchlist/by-summoner/{summonerId}',
    match='v2.2/match/{matchId}',
    recent_games='v1.3/game/by-summoner/{summonerId}/recent',
    ranked_stats='v1.3/stats/by-summoner/{summonerId}/ranked',
    summary_stats='v1.3/stats/by-summoner/{summonerId}/summary',
    league_data='v2.5/league/by-summoner/{summonerId}'
)

# default number of seconds to wait when given a RateLimitExceeded exception
RATE_LIMIT_EXCEEDED_SLEEP_DURATION = 10


class Client:

    def __init__(self, api_key: str=None):

        if api_key:
            self._api_key = api_key
        else:
            raise Exception('api_key not set')
        self.base = 'https://{region}.api.pvp.net/api/lol/{region}/'

    @staticmethod
    def _handle_status(r):

        if r.status_code == requests.codes.ok:
            return True
        elif r.status_code == requests.codes.too_many_requests:
            time.sleep(int(r.headers.get('Retry-After',
                                         RATE_LIMIT_EXCEEDED_SLEEP_DURATION)))
            return False
        else:
            # TODO Delete or rework for your own use
            # Following code is how I track errors with my application
            # error_format = 'Url={url},' \
            #                'Status_code={status_code},' \
            #                'Content={content}'
            # error_details = error_format.format(
            #     url=r.url,
            #     status_code=r.status_code,
            #     content=r.text
            # )
            # http_error_msg = ''
            #
            # if 400 <= r.status_code < 500:
            #     http_error_msg = '%s Client Error: %s' % (
            #         r.status_code, r.reason)
            #
            # elif 500 <= r.status_code < 600:
            #     http_error_msg = '%s Server Error: %s' % (
            #         r.status_code, r.reason)
            #
            # lolcoachextensions.services.error_logger.ErrorLogger().log_error(
            #     'RiotApi.Client',
            #     requests.HTTPError(http_error_msg, response=r),
            #     error_details
            # )
            r.raise_for_status()

    def get_summoner_by_name(self, summoner_name: str, region: str='na'):

        assert type(summoner_name) is str, \
            'summoner_name is not a string: %r' % str(summoner_name)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        url = (self.base + URLS['summoner_by_name']).format(
            region=region,
            summonerName=summoner_name
        )
        payload = {'api_key': self._api_key}
        r = requests.get(url, params=payload)
        if not self._handle_status(r):
            return self.get_summoner_by_name(summoner_name, region)

        return r.json()

    def get_summoner_by_id(self, summoner_id: Any, region: str='na'):

        assert type(summoner_id) is int or type(
            summoner_id) is str, \
            'summoner_id is not an int or str: %r' % str(summoner_id)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        url = (self.base + URLS['summoner_by_id']).format(
            region=region,
            summonerId=summoner_id
        )
        payload = {'api_key': self._api_key}
        r = requests.get(url, params=payload)
        if not self._handle_status(r):
            return self.get_summoner_by_id(summoner_id, region)

        return r.json()

    def get_summoners_by_names(
            self,
            summoner_names:
            List[str],
            region: str='na'
    ):

        assert type(summoner_names) is list, \
            'summoner_names is not a list: %r' % str(summoner_names)
        assert type(summoner_names[0]) is str, \
            'summoner_names is not a list of strings: %r' % str(summoner_names)
        assert 0 < len(summoner_names) <= 40, \
            'summoner_names can only have 40 names, has: %r' % \
            str(len(summoner_names))
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        return self.get_summoner_by_name(','.join(summoner_names), region)

    def get_summoners_by_ids(
            self,
            summoner_ids: List[int],
            region: str='na'
    ):

        assert type(summoner_ids) is list, \
            'summoner_ids is not a list: %r' % str(summoner_ids)
        assert type(summoner_ids[0]) is int, \
            'summoner_ids is not a list of ints: %r' % str(summoner_ids)
        assert 0 < len(summoner_ids) <= 40, \
            'summoner_ids can only have 40 ids, has: %r' % \
            str(len(summoner_ids))
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        return self.get_summoner_by_id(
            ','.join([str(s_id) for s_id in summoner_ids]), region
        )

    def get_match_list(
        self,
        summoner_id: int,
        region: str='na',
        begin_time: int=0
    ):

        assert type(summoner_id) is int, \
            'summoner_id is not an int: %r' % str(summoner_id)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        url = (self.base + URLS['match_list']).format(
            region=region,
            summonerId=summoner_id
        )
        payload = {'api_key': self._api_key}
        if begin_time and begin_time > 0:
            payload.update({'beginTime': begin_time})

        r = requests.get(url, params=payload)
        if not self._handle_status(r):
            return self.get_match_list(summoner_id, region)

        return r.json()

    def get_match(
            self, match_id: int,
            include_timeline: bool=False,
            region: str='na'
    ):

        assert type(match_id) is int, \
            'match_id is not an int: %r' % str(match_id)
        assert type(include_timeline) is bool, \
            'include_timeline is not a bool: %r' % str(include_timeline)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        url = (self.base + URLS['match']).format(
            region=region,
            matchId=match_id
        )
        payload = {
            'api_key': self._api_key,
            'includeTimeline': include_timeline
        }
        r = requests.get(url, params=payload)
        if not self._handle_status(r):
            return self.get_match(match_id, include_timeline, region)

        return r.json()

    def get_recent_games(self, summoner_id: int, region: str='na'):

        assert type(summoner_id) is int, \
            'summoner_id is not an int: %r' % str(summoner_id)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        url = (self.base + URLS['recent_games']).format(
            region=region,
            summonerId=summoner_id
        )
        payload = {'api_key': self._api_key}
        r = requests.get(url, params=payload)
        if not self._handle_status(r):
            return self.get_recent_games(summoner_id, region)

        return r.json()

    def get_ranked_stats(self, summoner_id: int, region: str='na'):

        assert type(summoner_id) is int, \
            'summoner_id is not an int: %r' % str(summoner_id)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        url = (self.base + URLS['ranked_stats']).format(
            region=region,
            summonerId=summoner_id
        )
        payload = {'api_key': self._api_key}
        r = requests.get(url, params=payload)
        if not self._handle_status(r):
            return self.get_ranked_stats(summoner_id, region)

        return r.json()

    def get_summary_stats(
            self,
            summoner_id: int,
            region: str='na'
    ):

        assert type(summoner_id) is int, \
            'summoner_id is not an int: %r' % str(summoner_id)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        url = (self.base + URLS['summary_stats']).format(
            region=region,
            summonerId=summoner_id
        )
        payload = {'api_key': self._api_key}
        r = requests.get(url, params=payload)
        if not self._handle_status(r):
            return self.get_summary_stats(summoner_id, region)

        return r.json()

    def get_league_data(self, summoner_id: Any, region: str='na'):

        assert type(summoner_id) is int or type(summoner_id) is str, \
            'summoner_id is not an int or str: %r' % str(summoner_id)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        url = (self.base + URLS['league_data']).format(
            region=region,
            summonerId=summoner_id
        )
        payload = {'api_key': self._api_key}
        r = requests.get(url, params=payload)
        if not self._handle_status(r):
            return self.get_league_data(summoner_id, region)

        return r.json()

    def get_league_data_multiple_summoners(
            self,
            summoner_ids: List[int],
            region: str='na'
    ):

        assert type(summoner_ids) is list, \
            'summoner_ids is not a list: %r' % str(summoner_ids)
        assert type(region) is str, \
            'region is not a string: %r' % str(region)

        return self.get_league_data(
            ','.join([str(summoner_id)
                      for summoner_id in summoner_ids]
                     ), region)


if __name__ == '__main__':
    c = Client()
    me = c.get_summoner_by_name('drunk7irishman')
    test = c.get_ranked_stats(me['drunk7irishman']["id"])
    test2 = c.get_league_data(me['drunk7irishman']["id"])
    print(test)
