import requests
import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup as bs
import time

BASKETBALL_REFERENCE = "https://www.basketball-reference.com"

def _get_path(name):
    if name == "james lebron":
        name = "j/jamesle01"
    else:
        raise Exception
    return name

def game_log_endpoint(name, year=2004, advanced=False):
    url = f"https://www.basketball-reference.com/players/{name}/gamelog-advanced/{year}/"
    if not advanced:
        url = f"https://www.basketball-reference.com/players/{name}/gamelog/{year}/"
    return url

def player_endpoint(alpha):
    url = f"https://www.basketball-reference.com/players/{alpha}"
    return url


def parse_player_row(row):
    row_data = {}
    for child in row.children:
        try: 
            stat = child["data-stat"]
            if stat == "player":
                row_data[stat] = child.get_text()
                row_data["player_url"] = child.find("a")["href"]
                if child.find("strong"):
                    row_data["active"] = True
                else:
                    row_data["active"] = False
            else:
                row_data[stat] = child.get_text()
        except TypeError as e:
            pass
    return row_data

def get_player_list(alpha):
    url = player_endpoint(alpha)
    resp = requests.get(url)
    soup = bs(resp.content, 'html.parser')
    table = soup.find("table")
    trs = table.find_all('tr')
    # remove the header
    trs = trs[1:]
    data = [parse_player_row(tr) for tr in trs]
    df = pd.DataFrame.from_records(data)
    return df

def get_game_logs(name, year, advanced=False):
    url = game_log_endpoint(name, year, advanced)
    resp = requests.get(url)
    table = pd.read_html(resp.content)
    df = table[0]
    # remove headers in the middle
    df = df[df['Date'] != "Date"]
    return df

def get_game_logs_from_path(path):
    url = BASKETBALL_REFERENCE + path
    print(url)

    resp = requests.get(url)
    try:
        id = "pgl_basic"
        if "gamelog-advanced" in path:
            id = "pgl_advanced"
        table = pd.read_html(resp.content, attrs={"id": id})
        df = table[-1]    
        # remove headers in the middle
        df = df[df['Date'] != "Date"]
        return df, resp.from_cache
    except Exception as e:
        print(e)
        print(url)

def get_game_logs_all(name, all_path, advanced=False, new_only=False, no_remote=False):
    data = []
    if not no_remote:
        if new_only:
            all_path = all_path[-1:]
        for path in all_path:
            if advanced:
                path = path.replace("/gamelog/", "/gamelog-advanced/")
            dat = get_game_logs_from_path(path)
            if dat and isinstance(dat[0], pd.DataFrame):
                data.append(dat[0])
                if not dat[1]:
                    time.sleep(2)
        df = pd.concat(data)
        last_name = name.split(" ")[-1]
        name = name.replace(" ", "_")
        name = last_name + "_" + name
        if advanced:
            ori_df = pd.read_csv(f"data/player_gamelogs_advanced/{name}.csv")
            new_df = pd.concat([ori_df, df], ignore_index=True).drop_duplicates()
            new_df.to_csv(f"data/player_gamelogs_advanced/{name}.csv", index=False)
        else:
            ori_df = pd.read_csv(f"data/player_gamelogs/{name}.csv")
            new_df = pd.concat([ori_df, df], ignore_index=True).drop_duplicates()
            new_df.to_csv(f"data/player_gamelogs/{name}.csv", index=False)
        return new_df
    else:
        last_name = name.split(" ")[-1]
        name = name.replace(" ", "_")
        name = last_name + "_" + name
        if advanced:
            return pd.read_csv(f"data/player_gamelogs_advanced/{name}.csv")
        else:
            return pd.read_csv(f"data/player_gamelogs/{name}.csv")


__cache = {}
def get_soup(url):
    if not url in __cache:
        __cache[url] = requests.get(url)
        _resp = __cache[url]
        if _resp.status_code != 200:
            raise Exception
    else:
        _resp = __cache[url]
    soup = bs(_resp.content, "html.parser")
    return soup

def get_available_years(player_path):
    url = "http://www.basketball-reference.com" + player_path
    soup = get_soup(url)
    available_year = soup.find_all(string="Game Logs")
    available_year_ul = available_year[0].parent.parent.parent.find("ul").find_all("a")
    paths = [x["href"] for x in available_year_ul if "playoffs" not in  x["href"]]
    return paths

def get_all_players(remote=False):
    if not remote:
        df = pd.read_csv("data/players_list/all_players.csv")
        return df
    import string
    data = []
    for alpha in string.ascii_lowercase:
        df = get_player_list(alpha)
        data.append(df)
        time.sleep(8)
    return data

def get_active_players():
    df = pd.read_csv("data/players_list/active_players.csv")
    return df

def get_year_links():
    years = get_available_years()
    years = [year['href'] for year in years if "playoffs" not in year["href"]]
    return years


def get_game_logs_range(name, start, end, advanced=False):
    df_list = []
    for year in range(start, end):
        df = get_game_logs(name, year)
        df_list.append(df)
    all_df = pd.concat(df_list, ignore_index=True, axis=0)
    return all_df

def get_game_logs_lebron():
    return get_game_logs_range("james lebron", 2004, 2024, advanced=True)


class Player:
    @property
    def game_logs():
        pass