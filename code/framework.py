import pandas as pd
from code.draftkings import get_leaderboard, get_contest_date, get_draftables_by_contest_id, get_contest_details

class FantasyModel:
    def __init__(self):
        self.context = ""

    @property 
    def contest(self):
        # return current contest information
        return

    @property
    def drafts(self):
        return # players choice for current contest

    @property
    def player_logs(self):
        return # player info upto contest time

class MyModel(FantasyModel):
    def generate_lineup(self):
        pass

    def join_contest(self):
        pass

class StupidModel(FantasyModel):
    def generate_lineup(self, lineups):
        # lineup = random(self.drafts)
        # print(lineups)
        return lineups

    def join_contest(self, contest_id):
        # decision = decide_based_on(self.contest, self.game, self.drafts)
        return True

class Simulator:
    def __init__(self):
        pass

def estimate_leaderboard_placement(leaderboard, fantasy_points):
    ind = len(leaderboard[leaderboard["fantasyPoints"] >= fantasy_points])
    row = leaderboard.iloc[ind]
    return row

def calculate_winning(leaderboard, fp):
    row = estimate_leaderboard_placement(leaderboard, fp)
    return row["winningValue"]

def player_fp_by_date(player_name, date):
    from code.draftkings import get_player_logs
    logs = get_player_logs(player_name)
    logs = logs.loc[:, ~logs.columns.duplicated()]
    logs = logs[logs["Date"] == date]
    row = logs.iloc[0]
    points = float(row["PTS"]) * 1
    three_points = float(row["3P"]) * 0.5
    rebound = float(row["TRB"]) * 1.25
    assist = float(row["AST"]) * 1.5
    steal = float(row["STL"]) * 2
    block = float(row["BLK"]) * 2
    turnover = float(row["TOV"]) * -0.5
    fp = points + three_points + rebound + assist + steal + block + turnover
    return fp


def simulate(date_range):
    for date in date_range:
        contest_ids = get_contest_ids_by_date(date)
        for contest_id in contest_ids:
            simulate_contest(contest_id)

def simulate_draftkings_classic(contest_id, model):
    lineups = get_draftables_by_contest_id(contest_id).json()["draftables"]
    contest_data = get_contest_details(contest_id)
    join_contest = model.join_contest(contest_data)
    if join_contest:
        pred_lineup = model.generate_lineup(lineups)
        total_fp = 0
        contest_date = str(get_contest_date(contest_id).date())
        for player in pred_lineup:
            player_name = player["displayName"]
            try:
                actual_fp = player_fp_by_date(player_name, contest_date)
                total_fp += actual_fp
            except Exception as e:
                print(e)
                import traceback
                traceback.print_exc()
                print(player_name)
                print(player["firstName"])
                print(player["lastName"])
                
                print(contest_date)
        leaderboard = get_leaderboard(contest_id)["leaderBoard"]
        leaderboard = pd.DataFrame.from_records(leaderboard)
        winning = calculate_winning(leaderboard, total_fp)
        return winning

# model = StupidModel()
# simulate_draftkings_classic
# profit_loss = StupidModel(date_range=last_100_days).evaluate()