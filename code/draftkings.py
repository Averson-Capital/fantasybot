from progress.bar import Bar
import json
cookies = {
    'hgg': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2aWQiOiIyNTM5Mzg3MTEzMyIsImRrZS02MCI6IjI4NSIsImRrZS0xMjYiOiIzNzQiLCJka2UtMTQ0IjoiNDMxIiwiZGtlLTE0OSI6IjMzNzMiLCJka2UtMTUwIjoiNTY3IiwiZGtlLTE1MSI6IjQ1NyIsImRrZS0xNTIiOiI0NTgiLCJka2UtMTUzIjoiNDU5IiwiZGtlLTE1NCI6IjQ2MCIsImRrZS0xNTUiOiI0NjEiLCJka2UtMTU2IjoiNDYyIiwiZGtlLTE3OSI6IjU2OSIsImRrZS0yMDQiOiI3MTAiLCJka2UtMjE5IjoiMjI0NiIsImRraC0yMjkiOiJJbE5oQzA2UyIsImRrZS0yMjkiOiIwIiwiZGtlLTIzMCI6Ijg1NyIsImRrZS0yODgiOiIxMTI4IiwiZGtlLTMwMCI6IjExODgiLCJka2UtMzE4IjoiMTI2MCIsImRrZS0zNDUiOiIxMzUzIiwiZGtlLTM0NiI6IjEzNTYiLCJka2gtMzk0IjoiQ2ZYQWh6ZE8iLCJka2UtMzk0IjoiMCIsImRraC00MDgiOiJZZGFWUm1EWiIsImRrZS00MDgiOiIwIiwiZGtlLTQxNiI6IjE2NDkiLCJka2UtNDE4IjoiMTY1MSIsImRrZS00MTkiOiIxNjUyIiwiZGtlLTQyMCI6IjE2NTMiLCJka2UtNDIxIjoiMTY1NCIsImRrZS00MjIiOiIxNjU1IiwiZGtlLTQyOSI6IjE3MDUiLCJka2UtNzAwIjoiMjk5MiIsImRrZS03MzkiOiIzMTQwIiwiZGtlLTc1NyI6IjMyMTIiLCJka2gtNzY4IjoiVVpHYzBySHgiLCJka2UtNzY4IjoiMCIsImRrZS03OTAiOiIzMzQ4IiwiZGtlLTc5NCI6IjMzNjQiLCJka2UtODA0IjoiMzQxMSIsImRrZS04MDYiOiIzNDI1IiwiZGtlLTgwNyI6IjM0MzciLCJka2UtODI0IjoiMzUxMSIsImRrZS04MjUiOiIzNTE0IiwiZGtlLTgzNCI6IjM1NTciLCJka2UtODM2IjoiMzU3MCIsImRrZS04NjUiOiIzNjk1IiwiZGtoLTg5NSI6IjJ6MERZU0MyIiwiZGtlLTg5NSI6IjAiLCJka2UtOTAzIjoiMzg0OCIsImRrZS05MTciOiIzOTEzIiwiZGtlLTkzOCI6IjQwMDQiLCJka2UtOTQ3IjoiNDA0MiIsImRrZS05NzYiOiI0MTcxIiwiZGtlLTEwODEiOiI0NTg3IiwiZGtlLTExMDQiOiI0Njc2IiwiZGtlLTExMjQiOiI0NzY0IiwiZGtlLTExMjYiOiI0NzY4IiwiZGtoLTExMjkiOiIyOG1oZWZvcCIsImRrZS0xMTI5IjoiMCIsImRrZS0xMTcyIjoiNDk2NCIsImRrZS0xMTczIjoiNDk2NyIsImRrZS0xMTc0IjoiNDk3MCIsImRrZS0xMTg3IjoiNTAxNSIsImRrZS0xMjEwIjoiNTEyNyIsImRrZS0xMjEzIjoiNTE0MiIsImRrZS0xMjMxIjoiNTIxMyIsImRrZS0xMjQ0IjoiNTI2NyIsImRrZS0xMjU1IjoiNTMyNiIsImRrZS0xMjU5IjoiNTMzOSIsImRrZS0xMjYxIjoiNTM0OSIsImRrZS0xMjc3IjoiNTQxMSIsImRrZS0xMjgwIjoiNTQyNyIsImRrZS0xMjg3IjoiNTQ1OCIsImRrZS0xMjkwIjoiNTQ3NCIsImRrZS0xMjk1IjoiNTQ5NSIsImRrZS0xMjk5IjoiNTUwOSIsImRraC0xMzAzIjoiLUxrekFyZUsiLCJka2UtMTMwMyI6IjAiLCJka2gtMTMwNCI6IkFCSDhqM1hUIiwiZGtlLTEzMDQiOiIwIiwiZGtoLTEzMDciOiJ4UTBTSHNZOCIsImRrZS0xMzA3IjoiMCIsImRraC0xMzA4IjoiLTFHR2xmdGsiLCJka2UtMTMwOCI6IjAiLCJka2UtMTMxNCI6IjU1NzIiLCJka2UtMTMyMyI6IjU2MjYiLCJka2UtMTMyNSI6IjU2MzkiLCJka2UtMTMyNyI6IjU2NTEiLCJka2UtMTMyOCI6IjU2NTMiLCJuYmYiOjE2Njk5MjI1OTIsImV4cCI6MTY2OTkyMjg5MiwiaWF0IjoxNjY5OTIyNTkyLCJpc3MiOiJkayJ9._IGFBNeN2fZDI5cnB6LCmXOQjjLHVs6OlbsDgEhFofc',
    'STE': '"2022-12-01T19:56:01.4520254Z"',
    'STIDN': 'eyJDIjoxMjIzNTQ4NTIzLCJTIjo0MTQ3ODE3OTM3MCwiU1MiOjQzNjc3NzE0OTMwLCJWIjoyNTM5Mzg3MTEzMywiTCI6MSwiRSI6IjIwMjItMTItMDFUMTk6NDc6NTUuNDg5NzY4M1oiLCJTRSI6IlVTLURLIiwiVUEiOiJrVTdSWDFDekFkYnAxZ1VMS2ovdzlFME4rR0N1YkJscXJzUzZCTllwVVFRPSIsIkRLIjoiNzI2YzU3MzktYjBiNC00M2UyLWIyNDItMWFkMzg3YjU3OTRkIiwiREkiOiJiOWY2ODhmNC00MDIxLTRhZjAtOTY0ZS02MjdiN2U3MDM0NzAiLCJERCI6MjEyMDU0NzM1MDZ9',
    'STH': '9d1d2138207918c650e4710d14396dac8e686709f60b1e9973b22027d4c91c0f',
    '_abck': '34949E7733B9C6AF1B7A96059294AE88~-1~YAAQH+x7XBtnG4yEAQAA7S0nzwgpzPgBA72h54m/Z4gCgYTSxlxGHPeYQ45qJtkuASw0/n/e5zSIxI7t1eFkUd/p7kq6BlZu80VhepsjAk94WnzsAAOlEpiHGIa//4z5IEPIWldjrYyoTv+TndK+0vMj4rUFPmxD6hg6s8YvQ9/D6py5L+8Yl/bVYzraOzse3zg4KgV8dQ1N/gQbW6ZHT7mWkyDr8UYgDccrXkX9zJvvw0J2j/gFOsP0eVlUMalTBoMLgpxHAN6jZS8jfgfeNljuugyNZp8qA6xt8KBpDz6Bsg+kCm4EcBYjI1ZSDfxzqvEV/SiuOlj+Rrx1em7dK6yNl0V+BnqD+cNV8/EHU3fT7qLYCdc/175aAtU2bwrZhhnBAF398aDw1JSoJdvvRbbErY45+aIQIpV9mQ==~0~-1~-1',
    'VIDN': '25393871133',
    'SN': '1223548523',
    'LID': '1',
    'SINFN': 'PID=&AOID=&PUID=26711549&SSEG=&GLI=0&LID=1&site=US-DK',
    'PRV': '3P=0&V=25393871133&E=1670008659',
    'ss-pid': 'UBp3gSXHUTF4BbNvpZUg',
    'site': 'US-DK',
    'SIDN': '41478179370',
    'SSIDN': '43677714930',
    'EXC': '43677714930:73',
    'ak_bmsc': '51349FED81D259D8B9B8214BE6D35650~000000000000000000000000000000~YAAQlRwhF7Oi8K+EAQAA9lQTzxGgaGXy74Sr/hNZqU374PShokkrJbSElvoalCpmQgmwkXPaq4oejvTG2w4y3KDEot2hTSOztjdnRCLCkBJrHJkMVr6oEcgOwEY5sf3nE7RnDk3qmFLVP6REZS9/oCai14kXKLvtcwFSuojeXGdnPxKppjP7Dr7T00Yf2xZYFBkOfEtNCasbeR0ht8rsCLuLcnK+Vy7V8FK6prEPNKl9eIBbqghvEcglnNpascSNAktAvW+V/+T3h3lnzSRjPQ4U9oe6p1e3pyYRV7zxu7mCjxbHHvvOI1W/vQJAFa05Bk51vCvPrHjUg0XnvKQBDGQDnmtlwjQLA5yItv1/J1k9GtoLQ3Hf+cP9PxjTquivQadpOvd0iX8v6M1XPo8=',
    'bm_sz': 'B19167A5EFBA07087A6C1958F9AD2F55~YAAQlRwhF7Si8K+EAQAA9lQTzxGRDOLf/x7t6OF6WH/JD5E4mhOVtgpuCcqrlRtS+2BpiFe4dPb4GPF1zcLEJyLrKK3xhkd08x8cvVY6f6iEJZSholdVjEW/DS6+arTqag6nAaFoTtw76ZGK6EXHSzX6bkkM1WPAZDGguRIn4ntqrG5ro2T3vdSH6EyVYbSXaVmMPowCrAlLQez8vzx+WHwBmMTQaSilzZu1H8o9aiPFXpAJRIcMUBk834tg0saBe1dO/IulY1taiDud9M6k605WeX6j7uKjujQdzqmE5IFIlhVgSydw~4277815~4539705',
    'bm_sv': '86B697FAC6876D243EB6DABF7F51CB59~YAAQH+x7XBBnG4yEAQAAOCsnzxEA8oFVHG9QPEA2Sf+inR5mWPrTAsrn4Wu0/WGrrCuSLaCFUR6seGqeou0yBI4rQyCY9MSs6wbwYeKoNu3vQfbbmJeZ3Ik/iUmg0bo05Tf/iIPPwbJX91ABO6EhhR0DKaZaNGQ9Lx56JmhoO7cWWDDIDI3h440CqRN/UOr4E3NVXT8Xw16QtxjHJnsyPetDZSGlaHKAWCYw4SGXc6FIOg6+p1505jC6sZD79HlXK/WEIMIl~1',
    '_csrf': '7515b090-5748-4c1f-a906-bd180ad820c9',
    'ASP.NET_SessionId': 'ruo33sq0jixjcxtz2mnveknm',
    'jwe': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImN0eSI6IkpXVCIsInZlcnNpb24iOiIxIn0.eyJ1bmlxdWVfbmFtZSI6Im5hdHZlazMzMzMiLCJ1ayI6IjFlMTk1YzEyLTYxODgtNDZiOC05MjFmLTRhODNmYmEyY2FiZCIsInJvbGUiOiJOb3JtYWwiLCJlbWFpbCI6Im5hdHZlazIyMjJAb3V0bG9vay5jb20iLCJyYWZpZCI6IiIsInZpZCI6IjI1MzkzODcxMTMzIiwibGlkIjoiMSIsImppZCI6IjE2OTUxNDUwNTU2IiwiamtleSI6ImN1cnJlbnQiLCJmdGRiZSI6IlRydWUiLCJnZW8iOiIiLCJmdnMiOiIzIiwiY2RhdGUiOiIyMDIyLTEyLTAxIDE5OjE3OjM4WiIsImN1ciI6IlVTRCIsIml2IjoiaGgzaGJycEY5NmVIK1JlVHNQTm54Zz09IiwiZXVpZCI6Ilgrc1pvVzNiNStvNU5LRkt3MFltUlE9PSIsIkRLUC1EZW55QWxsQ29udGVzdHMiOiJ0cnVlIiwiREtQLURlbnlEZXBvc2l0IjoidHJ1ZSIsIkRLUC1EZW55V2l0aGRyYXdhbCI6InRydWUiLCJES1AtRGVueUFsY29ob2xQcm9tb3MiOiJ0cnVlIiwiREtQLVZpZXdEZnMiOiJ0cnVlIiwiREtQLVZpZXdNYXJrZXRwbGFjZSI6InRydWUiLCJhdXRoIjoiYjlhODhiNWEtZWY3Yi00YjQxLWE4NTctMjQ5ZDgzZGM2NDZlIiwibHQiOiJkcmFmdGtpbmdzIiwic2J0IjoiNTIzNjUzMjIiLCJuYmYiOjE2Njk5MjI1OTIsImV4cCI6MTY2OTkyMjg5MiwiaXNzIjoidXJuOmRrL2NlcmJlcnVzIiwiYXVkIjoidXJuOmRrIn0.2GJtc0bGzrDjp8N9-Ti5w70-_kYpLm8WaiC0BEMTKng',
    'iv': 'e2DDlYHyknKGsv4pyAge3kINk0ROswZx140vi4pQc4M=',
    'uk': '1',
    'mlc': 'true',
    'notice_behavior': 'implied,eu',
    'notice_preferences': '2:',
    'notice_gdpr_prefs': '0,1,2::implied,eu',
    'cmapi_gtm_bl': '',
    'cmapi_cookie_privacy': 'permit 1,2,3',
}

import requests
import requests_cache
requests_cache.install_cache("my_cache", backend="sqlite")

proxy = {"http": "192.168.86.235:36343", "https": "192.168.86.235:36343"}

def get_contest_details(id):
    url = f"https://api.draftkings.com/contests/v1/contests/{id}?format=json"
    resp = requests.get(url, proxies=proxy)
    return resp

def get_contest_date(contest_id):
    from dateutil.parser import isoparse
    import pytz
    detail = get_contest_details(contest_id)
    date = detail.json()["contestDetail"]["contestStartTime"]
    date = isoparse(date)
    return date.astimezone(pytz.timezone("EST"))

def get_draft_group_id(contest_id):
    resp = get_contest_details(contest_id)
    return resp.json()['contestDetail']['draftGroupId']

def get_draftables_by_contest_id(contest_id):
    draft_id = get_draft_group_id(contest_id)
    url = f"https://api.draftkings.com/draftgroups/v1/draftgroups/{draft_id}/draftables?format=json"
    resp = requests.get(url, proxies=proxy)
    return resp

def get_draftables_by_draft_id(draft_id):
    url = f"https://api.draftkings.com/draftgroups/v1/draftgroups/{draft_id}/draftables?format=json"
    resp = requests.get(url, proxies=proxy)
    return resp

def get_leaderboard_and_lineups(index, contest_id):
    url = f"https://api.draftkings.com/scores/v1/leaderboards/{contest_id}?format=json&embed=leaderboard"
    resp = requests.get(url, cookies=cookies, proxies=proxy)
    data = resp.json()
    try:
        data["lineups"] = get_draftables_by_draft_id(data["leader"]["draftGroupId"]).json()
        with open(f"data/draftkings_contest_data_new_5000/{index}_{contest_id}_leaderboard.json", "w") as f:
            import json
            f.write(json.dumps(data))
        return data
    except Exception:
        return

def get_leaderboard(contest_id):
    url = f"https://api.draftkings.com/scores/v1/leaderboards/{contest_id}?format=json&embed=leaderboard"
    resp = requests.get(url, cookies=cookies, proxies=proxy)
    data = resp.json()
    return data

def get_fantasy_cruncher_contest_data():
    import pandas as pd
    df_arr = []
    for year in range(2016, 2023):
        df = pd.read_csv(f"data/consolidated_data/fantasy_cruncher_{year}.csv")
        df_arr.append(df)
    data = pd.concat(df_arr)
    return data


def get_past_contest_lineups():
    data = get_fantasy_cruncher_contest_data()
    filtered_data = data[data["site"].isin(["draftkings"])]
    site_ids = filtered_data[["site", "site_id"]]
    for row in site_ids.iloc[-5000:].iterrows():
        site_id = row[1]["site_id"]
        get_leaderboard_and_lineups(row[0], site_id)
        import time
        time.sleep(10)

def get_entries(contest_id):
    info = get_leaderboard(contest_id)
    draft_id = info["leader"]["draftGroupId"]
    data = []
    for item in info["leaderBoard"]:
        entry_id = item["entryKey"]
        url = f"https://api.draftkings.com/scores/v2/entries/{draft_id}/{entry_id}?format=json&embed=roster"
        print(url)
        resp = requests.get(url, cookies=cookies, proxies=proxy)
        data.append(resp.json())
    return data

def get_entry(draft_id, entry_key):
    url = f"https://api.draftkings.com/scores/v2/entries/{draft_id}/{entry_key}?format=json&embed=roster"
    resp = requests.get(url, cookies=cookies, proxies=proxy)
    data = resp.json()
    print(resp.from_cache)
    return data

def to_parquet(fn):
    def wrapper(arg):
        df = fn(arg)
        df.to_parquet(f"data/parquet/{fn.__name__}_{arg}.parquet")
        return df
    return wrapper

def get_leaderboards_by_date(date):
    contest_ids = get_contest_ids_by_date(date)
    # dfs = []
    total = len(contest_ids)
    count = 0
    with Bar('Processing', max=total) as bar:
        for id in contest_ids:
            count += 1
            # print(f"{count}/{total}", end=" ")
            try:
                import os
                dir_path = f"data/parquet/leaderboards/{date}"
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                file_path = dir_path + f"/leaderboards_{id}.parquet"
                if not os.path.exists(file_path):
                    data = get_leaderboard(id)
                    df = pd.DataFrame.from_records(data["leaderBoard"])
                    df.to_parquet(file_path)
                bar.next()
            except Exception as e:
                print(e)
                print(data)
    return []

# start, end is date string like "2021-12-31"
def get_past_leaderboards(start, end):
    date_range = pd.date_range(start, end).to_pydatetime()
    for date in date_range:
        date = str(date.date())
        print(date)
        get_leaderboards_by_date(date)


import requests
import requests_cache
import pandas as pd

requests_cache.install_cache("my_cache", backend="sqlite")

def get_contest_today():
    response = requests.get('https://www.draftkings.com/lobby/getcontests')
    if response.status_code >= 200:
        df = pd.DataFrame.from_records(response.json()["Contests"])
        return df


def get_draft_group_id_from_contest_ids(contest_ids):
    contest = {}
    for id in contest_ids:
        draft_id = get_draft_group_id(id)
        info = get_draft_info(draft_id).json()
        sport = info["draftGroup"]["contestType"]["sport"]
        if sport == "NBA":
            contest[id] = draft_id
    unique_draft_id = {}
    for k, v in contest.items():
        if v not in unique_draft_id:
            unique_draft_id[v] = [k]
        else:
            unique_draft_id[v].append(k)
    return unique_draft_id


def get_draftgroup(limit=None, date=None):
    if date:
        contest_ids = get_contest_ids_by_date(date)
    else:
        today = get_contest_today()
        today = today[today["n"].str.contains("NBA")]
        contest_ids = today["id"]
    draftgroups = get_draft_group_id_from_contest_ids(contest_ids)
    draftgroups_obj = []
    arr = draftgroups.items()
    if limit:
        arr = list(arr)[0:limit]
    for draft_group_id, contest_ids in arr:
        draftgroup = DraftGroup(id=draft_group_id, contest_ids=contest_ids)
        draftgroups_obj.append(draftgroup)
    return draftgroups_obj


def get_contest_ids_by_date(date):
    from code.get_fantasy_cruncher import get_fantasy_cruncher_by_date
    resp = get_fantasy_cruncher_by_date(date)
    data = resp.json()
    contest_ids = [x["site_id"] for x in data if "draftkings" in x["site"]]
    return contest_ids

class DraftGroup:
    def __init__(self, id, contest_ids):
        self.contest_ids = contest_ids
        self.id = id
        self.draftables_data = get_draftables_by_draft_id(self.id)
        self.draftgroup_data = get_draft_info(self.id)

    def draftables_df(self):
        ids = ", ".join([str(x) for x in self.contest_ids])
        df = pd.DataFrame.from_records(self.draftables_data.json()["draftables"])
        df["contest_ids"] = ids
        def fppg(x):
            value = list(filter(lambda y: y["id"] == 219, x))[0]["value"]
            return value
        def oprk(x):
            value = list(filter(lambda y: y["id"] == -2, x))[0]["value"]
            return value
        df["draft_group_id"] = self.id
        df["fppg"] = df["draftStatAttributes"].map(fppg)
        df["oprk"] = df["draftStatAttributes"].map(oprk)
        return df

    def __repr__(self):
        games = self.draftgroup_data.json()["draftGroup"]["games"]
        games = [f"game_id={x['gameId']} {x['description']}" for x in games]
        return f"<DraftGroup draftkings id={self.id} {' '.join(games)}>"

    def print_contest_description(self):
        for id in self.contest_ids:
            summary = get_contest_details(id).json()["contestDetail"]["contestSummary"]
            print(summary)
            print(f"https://www.draftkings.com/contest/gamecenter/{id}")

    @staticmethod
    def get_todays_draftgroup(date=None, limit=None):
        requests_cache.install_cache("draftgroup_cache", backend="sqlite", allowable_methods=["GET", "POST"])
        draftgroups = get_draftgroup(date=date, limit=limit) #return an array of DraftGroup
        return draftgroups

    @classmethod
    def get_todays_lineup_df(cls, date=None, limit=None):
        from datetime import datetime
        draftgroups = cls.get_todays_draftgroup(date=date, limit=limit)
        df = []
        for draftgroup in draftgroups:
            print(draftgroup)
            # draftgroup.print_contest_description()
            df.append(draftgroup.draftables_df())
        all_lineups = pd.concat(df)
        if not date:
            date = str(datetime.now().date())
        all_lineups.to_csv(f"data/daily_draft_group/{date}.csv", index=False)
        return all_lineups




def get_draft_info(draft_id):
    resp = requests.get(f"https://api.draftkings.com/draftgroups/v1/{draft_id}?format=json")
    return resp


def draftkings_pipeline():
    draftgroups = get_draftgroup(1)
    for draft in draftgroups:
        print(draft)
        # lineups = data["lineups"]["draftables"]
        # contest_ids = data["contest_ids"]
    # for k, v in lineups.items():
    #     print(f"contest id: {k}")
    #     print(f"selectable players:")
    #     df = pd.DataFrame.from_records(v)
    #     print(df["displayName"])
    # gamelogs = get_lineup_gamelogs(lineups)
    # get game logs for each player in lineup
    # predict fantasy points for each player
    # run through optimizer
    return draftgroups

def get_lineup_gamelogs(lineups):
    unique_name = []
    data = {}
    array = list(lineups.items())
    total = len(array)
    count = 1
    for contest_id, draft_tables in list(lineups.items()):
        df = pd.DataFrame.from_records(draft_tables)
        # print(f"contest_id: {contest_id}")
        draft_id = get_draft_group_id(contest_id)
        # print(f"draft_id: {draft_id}")
        lineup_gamelogs = {}
        try:
            df = df[["displayName", "salary", "status", "position"]] 
            for name in df["displayName"]:
                # get game logs for this player
                if name not in unique_name:
                    unique_name.append(name)
            for name in unique_name:
                print(name)
            total_name = len(unique_name)
            name_count = 1
            for name in unique_name:
                print(f"draft group count: {count}/{total}")
                print(f"player count: {name_count}/{total_name}")
                name_count += 1
                gamelogs = get_player_info(name)
                lineup_gamelogs[name] = gamelogs
            print(df.head())
        except Exception as e:
            print(e)
            print(df)
            print(contest_id)
        data[draft_id] = lineup_gamelogs
        count += 1
    print(len(unique_name))
    return data

def get_player_logs(name):
    import difflib
    from code.get_basketball_reference import get_all_players, get_available_years, get_game_logs_all
    players = get_all_players()
    name = difflib.get_close_matches(name, players["player"])[0]
    df = players[players["player"] == name]
    player_path = df.iloc[0]["player_url"]
    # gamelogs_path = get_available_years(player_path)
    gamelogs_path = []
    df_advanced = get_game_logs_all(name, gamelogs_path, advanced=True, new_only=True, no_remote=True)
    df = get_game_logs_all(name, gamelogs_path, advanced=False, new_only=True, no_remote=True)
    return pd.concat([df, df_advanced], axis="columns")

def get_aws_creds():
    with open('data/aws_creds.json', 'r') as f:
        creds = json.load(f)
    return creds


def upload_parquet_s3(globb):
    import glob
    import boto3
    credentials = get_aws_creds()
    s3 = boto3.client('s3',
                      region_name = 'us-west-1',
                      **credentials
                      )
    S3_BUCKET = "kingsdraft-db"
    for path in glob.glob(globb):
        s3_path = path.replace("data/parquet/", "")
        print(s3_path)
        response = s3.upload_file(path, S3_BUCKET, s3_path)

def s3_client():
    import boto3
    credentials = get_aws_creds()
    s3 = boto3.client('s3',
                      region_name = 'us-west-1',
                      **credentials
                      )
    return s3