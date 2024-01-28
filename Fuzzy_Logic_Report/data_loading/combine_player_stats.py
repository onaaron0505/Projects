import os
import json
import copy

i = 6
combined_data =[]
while i <= 16:
    data = []
    with open(f'../data/2022_player_stats/week{i}.json', 'r') as file:
        data = json.load(file)
    week = data["week"]
    player_averages = data["players_averages"]
    defenses = data["teams"]
    player_actual = data["players_actual"]
    
    for id in player_actual:
        player = {}
        player["actual"] = player_actual[id]
        if id in player_averages and player_averages[id]['game'] > 4:
            player["averages"] = player_averages[id]
            position = player_averages[id]['position'].lower()
            if position == 'fb' or position == 'qb':
                continue
            defense = {
                "position_first_downs": defenses[player_averages[id]["opponent"]][f"{position}_first_downs"],
                "position_receptions": defenses[player_averages[id]["opponent"]][f"{position}_receptions"],
                "position_targets": defenses[player_averages[id]["opponent"]][f"{position}_targets"],
                "position_yards": defenses[player_averages[id]["opponent"]][f"{position}_yards"],
                "position_avg_yards": defenses[player_averages[id]["opponent"]][f"{position}_avg_yards"],
                "position_longest": defenses[player_averages[id]["opponent"]][f"{position}_longest"],
                "position_touchdowns": defenses[player_averages[id]["opponent"]][f"{position}_touchdowns"],
                "position_yards_after_catch": defenses[player_averages[id]["opponent"]][f"{position}_yards_after_catch"],
                "position_redzone_targets": defenses[player_averages[id]["opponent"]][f"{position}_redzone_targets"],
                "position_air_yards": defenses[player_averages[id]["opponent"]][f"{position}_air_yards"],
                "position_broken_tackles": defenses[player_averages[id]["opponent"]][f"{position}_broken_tackles"],
                "position_dropped_passes": defenses[player_averages[id]["opponent"]][f"{position}_dropped_passes"],
                "position_catchable_passes": defenses[player_averages[id]["opponent"]][f"{position}_catchable_passes"],
                "position_yards_after_contact": defenses[player_averages[id]["opponent"]][f"{position}_yards_after_contact"],
            }
            player["defense"] = defense
            combined_data.append(player)

    i += 1
with open(f'../data/2022_Stats.json', 'w') as json_file:
    json.dump(combined_data, json_file, indent=4)

i = 6
combined_data =[]
while i <= 8:
    data = []
    with open(f'../data/2023_player_stats/week{i}.json', 'r') as file:
        data = json.load(file)
    week = data["week"]
    player_averages = data["players_averages"]
    defenses = data["teams"]
    player_actual = data["players_actual"]
    
    
    for id in player_actual:
        player = {}
        player["actual"] = player_actual[id]
        if id in player_averages and player_averages[id]['game'] > 4:
            player["averages"] = player_averages[id]
            position = player_averages[id]['position'].lower()
            if position == 'fb' or position == 'qb':
                continue
            defense = {
                "position_first_downs": defenses[player_averages[id]["opponent"]][f"{position}_first_downs"],
                "position_receptions": defenses[player_averages[id]["opponent"]][f"{position}_receptions"],
                "position_targets": defenses[player_averages[id]["opponent"]][f"{position}_targets"],
                "position_yards": defenses[player_averages[id]["opponent"]][f"{position}_yards"],
                "position_avg_yards": defenses[player_averages[id]["opponent"]][f"{position}_avg_yards"],
                "position_longest": defenses[player_averages[id]["opponent"]][f"{position}_longest"],
                "position_touchdowns": defenses[player_averages[id]["opponent"]][f"{position}_touchdowns"],
                "position_yards_after_catch": defenses[player_averages[id]["opponent"]][f"{position}_yards_after_catch"],
                "position_redzone_targets": defenses[player_averages[id]["opponent"]][f"{position}_redzone_targets"],
                "position_air_yards": defenses[player_averages[id]["opponent"]][f"{position}_air_yards"],
                "position_broken_tackles": defenses[player_averages[id]["opponent"]][f"{position}_broken_tackles"],
                "position_dropped_passes": defenses[player_averages[id]["opponent"]][f"{position}_dropped_passes"],
                "position_catchable_passes": defenses[player_averages[id]["opponent"]][f"{position}_catchable_passes"],
                "position_yards_after_contact": defenses[player_averages[id]["opponent"]][f"{position}_yards_after_contact"],
            }
            player["defense"] = defense
            combined_data.append(player)

    i += 1

with open(f'../data/2023_Stats.json', 'w') as json_file:
    json.dump(combined_data, json_file, indent=4)
