import json

years = [2022, 2023]

for year in years:
    with open(f'../data/{year}_Schedule.json', 'r') as file:
        data = json.load(file)

    game_id_data = {"weeks": []}

    for idx, week in enumerate(data["weeks"]):
        game_ids = [game["id"] for game in week["games"] if game["status"] == "closed"]
        game_id_data["weeks"].append({"week": idx+1,"game_ids": game_ids})

    with open(f'../data/{year}_Game_Id.json', 'w') as json_file:
        json.dump(game_id_data, json_file, indent=4)

