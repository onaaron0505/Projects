import http.client
import json
import os
import time

conn = http.client.HTTPSConnection("api.sportradar.us")

years = [2022, 2023]

for year in years:
    with open(f'../data/{year}_Game_Id.json', 'r') as file:
        data = json.load(file)

    weeks = data["weeks"]
    for idx_week, week in enumerate(weeks):
        os.makedirs(f'../data/{year}_game_stats/week{idx_week+1}/', exist_ok=True)
        if idx_week < 16: # not using data for weeks 17 and 18 due to players sitting out at end of season
            for idx_game, game_id in enumerate(week["game_ids"]):
                conn.request("GET", f"http://api.sportradar.us/nfl/official/trial/v7/en/games/{game_id}/statistics.json?api_key=ms3n5mar4v3vj3dx6gqgvubq")
                res = conn.getresponse()
                data = res.read()

                data_object = json.loads(data.decode("utf-8"))
                with open(f'../data/{year}_game_stats/week{idx_week+1}/game{idx_game+1}.json', 'w') as json_file:
                    json.dump(data_object, json_file, indent=4)
                time.sleep(1)




