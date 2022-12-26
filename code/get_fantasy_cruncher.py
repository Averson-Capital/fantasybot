import pandas as pd
import requests
import datetime
import os
import time
import pathlib

def get_contest_links(start, end, year):
    date_range = pd.date_range(start=start, end=end)
    date_range = date_range.astype(str).to_list()
    # use curl cause too lazy to use requests and setup all the params
    # this command assumes you have curl."
    curl = "curl 'https://www.fantasycruncher.com/funcs/tournament-analyzer/get-contests.php' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://www.fantasycruncher.com' -H 'Connection: keep-alive' -H 'Referer: https://www.fantasycruncher.com/contest-links/NBA/2022-11-05' -H 'Cookie: PHPSESSID=g9lb71dveriuc63jmhec573g98; rememberMe=kevintandean%40gmail.com%3Ab973b473df8c1e7ec01418cdeba61d7b' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'TE: trailers' --data-raw 'sites%5B%5D=draftkings&sites%5B%5D=draftkings_pickem&sites%5B%5D=draftkings_showdown&sites%5B%5D=fanduel&sites%5B%5D=fanduel_single&sites%5B%5D=fanduel_super&sites%5B%5D=fantasydraft&sites%5B%5D=yahoo&sites%5B%5D=superdraft&leagues%5B%5D=NBA&periods%5B%5D={date}' -o {prefix}-{date}.json"
    # create dir if doesn't exist
    pathlib.Path(f'data/fantasycruncher/{year}').mkdir(parents=True, exist_ok=True) 
    for date in date_range:
        res = os.popen(curl.format(prefix=f"data/fantasycruncher/{year}/contest-data", date=date))
        # add sleep so it doesn't get blocked
        time.sleep(0.5)

def get_fantasy_contest_year(year):
    "get contest data for entire year from fantasycruncher.com"
    get_contest_links(f"1/1/{year}", f"12/31/{year}", year)



import os
import json

def load_existing_data(year):
    dir_path = f"data/fantasycruncher/{year}"
    path = "data/fantasycruncher/{}/{}"
    files = os.listdir(dir_path)
    empty = []
    good = []
    for file_name in files:
        file_path = path.format(year, file_name)
        with open(file_path, "r") as file_obj:
            try:
                data = json.load(file_obj)
                if len(data) < 1:
                    pass
                else:
                    good.append(data)
            except Exception:
                empty.append(file_name)
    return empty, good


def get_fantasy_cruncher_by_date(date):
    # need to update this periodically
    cookies = {
        'PHPSESSID': '1amivlkbc2cbcbuc7f65s79jpf',
    }

    # need to update this periodically
    headers = {
        'authority': 'www.fantasycruncher.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=1amivlkbc2cbcbuc7f65s79jpf',
        'origin': 'https://www.fantasycruncher.com',
        # 'pragma': 'no-cache',
        'referer': 'https://www.fantasycruncher.com/contest-links/NBA/2017-01-03',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'sites[]': [
            'draftkings',
            'draftkings_pickem',
            'draftkings_showdown',
            'fanduel',
            'fanduel_single',
            'fanduel_super',
            'fantasydraft',
            'yahoo',
            'superdraft',
        ],
        'leagues[]': 'NBA',
        'periods[]': date
    }
    response = requests.post('https://www.fantasycruncher.com/funcs/tournament-analyzer/get-contests.php', cookies=cookies, headers=headers, data=data)
    if response.status_code != 200:
        response.raise_for_status()
    import time
    if not response.from_cache:
        time.sleep(5)    
    from datetime import datetime
    dt_obj = datetime.strptime(date, "%Y-%m-%d")
    # with open(f"data/fantasycruncher/{dt_obj.year}/contest-data-{date}.json", "wb") as f:
    #     f.write(response.content)
    return response


def consolidate_data(year):
    df_arr = []
    err, good = load_existing_data(year)
    for dat in good:
        df = pd.DataFrame.from_records(dat)
        df_arr.append(df)
    df = pd.concat(df_arr)
    df.to_csv(f"fantasy_cruncher_{year}.csv")
