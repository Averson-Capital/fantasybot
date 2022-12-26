
import warnings 
warnings.filterwarnings('ignore')

import os

import datetime as dt
import json


import pandas as pd
import requests

with open('config/fantasydata.json', 'r') as f:
        fdata_creds = json.load(f)
        

def join_path(*args): 
    return '/'.join(args)

class fantasyData: 
    def __init__(self, api_key): 
        self.base_uri = 'https://api.sportsdata.io/api/nba/fantasy/json'
        self.api_key = api_key
        self.headers = {
            'Ocp-Apim-Subscription-Key' : self.api_key
        }

    def get_cur_season(self, params = {}): 
        uri = join_path(self.base_uri, 'CurrentSeason')
        print(uri)
        resp = requests.get(uri, headers = self.headers, params = params)
        return resp.json()
    
    def get_slate(self, date = dt.datetime.now().strftime('%Y-%b-%m'), operator = 'DraftKings', gametype = 'Classic'):
        uri = join_path(self.base_uri, 'DfsSlatesByDate', date)

        print(uri)
        resp = requests.get(uri, headers = self.headers)
        resp = pd.DataFrame(resp.json())
        resp = resp[(resp.Operator == operator) & (resp.OperatorGameType == gametype)]
        return resp
        
    def get_player_season_stats(self, season): 
        uri = join_path(self.base_uri, 'PlayerSeasonStats', str(season))
        print(uri)
        resp = requests.get(uri, headers = self.headers)
        return pd.DataFrame(resp.json())
    
    def get_player_projection_stats_by_date(self, date = dt.datetime.now().strftime('%Y-%b-%m')):
        uri = join_path(self.base_uri,'PlayerGameProjectionStatsByDate', date.upper())
        print(uri)
        resp = requests.get(uri, headers = self.headers)
        return pd.DataFrame(resp.json())

    def get_player_projection_stats_season(self, season = '2023'):
        uri = join_path(self.base_uri,'PlayerGameProjectionStatsByDate', season)
        print(uri)
        resp = requests.get(uri, headers = self.headers)
        return pd.DataFrame(resp.json())


        
        
