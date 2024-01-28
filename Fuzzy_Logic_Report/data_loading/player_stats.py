import os
import json
import copy

years = [2022, 2023]

for year in years: # each year
    player_stats = []
    team_stats = []
    player_actual = []
    schedule = []
    counter = 0
    week = 0
    for root, dirs, _ in os.walk(f'..\data\{year}_game_stats'): # each week
        for dir in dirs:
            player_stats.append({})
            player_actual.append({})
            team_stats.append({})
            schedule.append([])
            if week != 0:
                player_stats[week] = copy.deepcopy(player_stats[week - 1])
                team_stats[week] = copy.deepcopy(team_stats[week - 1])
            for root2, _, files in os. walk(os.path.join(root, f"week{week+1}")): # each game
                if len(files) == 0:
                    player_stats[week] = {}
                    team_stats[week] = {}
                for filename in files:
                    file_path = os.path.join(root2, filename)
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        # rushing_data = data["statistics"]["home"]["rushing"]["players"]
                        # rushing_data.extend(data["statistics"]["away"]["rushing"]["players"])
                    home = data["statistics"]["home"]["receiving"]["players"]
                    receiving_data = copy.deepcopy(home)
                    away = data["statistics"]["away"]["receiving"]["players"]
                    receiving_data.extend(copy.deepcopy(away))

                    home_id = data["summary"]["home"]["id"]
                    away_id = data["summary"]["away"]["id"]
                    schedule[week].append([home_id, away_id])
                    home_stats = {
                        "wr_first_downs": 0,
                        "wr_receptions": 0,
                        "wr_targets": 0,
                        "wr_yards": 0,
                        "wr_avg_yards": 0,
                        "wr_longest": 0,
                        "wr_touchdowns": 0,
                        "wr_yards_after_catch": 0,
                        "wr_redzone_targets": 0,
                        "wr_air_yards": 0,
                        "wr_broken_tackles": 0,
                        "wr_dropped_passes": 0,
                        "wr_catchable_passes": 0,
                        "wr_yards_after_contact": 0,
                        "te_first_downs": 0,
                        "te_receptions": 0,
                        "te_targets": 0,
                        "te_yards": 0,
                        "te_avg_yards": 0,
                        "te_longest": 0,
                        "te_touchdowns": 0,
                        "te_yards_after_catch": 0,
                        "te_redzone_targets": 0,
                        "te_air_yards": 0,
                        "te_broken_tackles": 0,
                        "te_dropped_passes": 0,
                        "te_catchable_passes": 0,
                        "te_yards_after_contact": 0,
                        "rb_first_downs": 0,
                        "rb_receptions": 0,
                        "rb_targets": 0,
                        "rb_yards": 0,
                        "rb_avg_yards": 0,
                        "rb_longest": 0,
                        "rb_touchdowns": 0,
                        "rb_yards_after_catch": 0,
                        "rb_redzone_targets": 0,
                        "rb_air_yards": 0,
                        "rb_broken_tackles": 0,
                        "rb_dropped_passes": 0,
                        "rb_catchable_passes": 0,
                        "rb_yards_after_contact": 0,
                    }
                    
                    away_stats = {
                        "wr_first_downs": 0,
                        "wr_receptions": 0,
                        "wr_targets": 0,
                        "wr_yards": 0,
                        "wr_avg_yards": 0,
                        "wr_longest": 0,
                        "wr_touchdowns": 0,
                        "wr_yards_after_catch": 0,
                        "wr_redzone_targets": 0,
                        "wr_air_yards": 0,
                        "wr_broken_tackles": 0,
                        "wr_dropped_passes": 0,
                        "wr_catchable_passes": 0,
                        "wr_yards_after_contact": 0,
                        "te_first_downs": 0,
                        "te_receptions": 0,
                        "te_targets": 0,
                        "te_yards": 0,
                        "te_avg_yards": 0,
                        "te_longest": 0,
                        "te_touchdowns": 0,
                        "te_yards_after_catch": 0,
                        "te_redzone_targets": 0,
                        "te_air_yards": 0,
                        "te_broken_tackles": 0,
                        "te_dropped_passes": 0,
                        "te_catchable_passes": 0,
                        "te_yards_after_contact": 0,
                        "rb_first_downs": 0,
                        "rb_receptions": 0,
                        "rb_targets": 0,
                        "rb_yards": 0,
                        "rb_avg_yards": 0,
                        "rb_longest": 0,
                        "rb_touchdowns": 0,
                        "rb_yards_after_catch": 0,
                        "rb_redzone_targets": 0,
                        "rb_air_yards": 0,
                        "rb_broken_tackles": 0,
                        "rb_dropped_passes": 0,
                        "rb_catchable_passes": 0,
                        "rb_yards_after_contact": 0,
                    }

                    wr_count = 0
                    te_count = 0
                    rb_count = 0
                    for player in home:
                        player_actual[week][player["id"]] = player
                        if not player["id"] in player_stats[week]: 
                            player_stats[week][player["id"]] = player
                            player_stats[week][player["id"]]["game"] = 1
                        else: 
                            player_stats[week][player["id"]]["first_downs"] = (player_stats[week][player["id"]]["first_downs"] * player_stats[week][player["id"]]["game"] + player["first_downs"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["receptions"] = (player_stats[week][player["id"]]["receptions"] * player_stats[week][player["id"]]["game"] + player["receptions"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["targets"] = (player_stats[week][player["id"]]["targets"] * player_stats[week][player["id"]]["game"] + player["targets"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["yards"] = (player_stats[week][player["id"]]["yards"] * player_stats[week][player["id"]]["game"] + player["yards"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["avg_yards"] = (player_stats[week][player["id"]]["avg_yards"] * player_stats[week][player["id"]]["game"] + player["avg_yards"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["longest"] = (player_stats[week][player["id"]]["longest"] * player_stats[week][player["id"]]["game"] + player["longest"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["touchdowns"] = (player_stats[week][player["id"]]["touchdowns"] * player_stats[week][player["id"]]["game"] + player["touchdowns"]) / (player_stats[week][player["id"]]["game"] + 1)
                            # player_stats[week][player["id"]]["longest_touchdown"] = (player_stats[week][player["id"]]["longest_touchdown"] * player_stats[week][player["id"]]["game"] + player["longest_touchdown"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["yards_after_catch"] = (player_stats[week][player["id"]]["yards_after_catch"] * player_stats[week][player["id"]]["game"] + player["yards_after_catch"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["redzone_targets"] = (player_stats[week][player["id"]]["redzone_targets"] * player_stats[week][player["id"]]["game"] + player["redzone_targets"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["air_yards"] = (player_stats[week][player["id"]]["air_yards"] * player_stats[week][player["id"]]["game"] + player["air_yards"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["broken_tackles"] = (player_stats[week][player["id"]]["broken_tackles"] * player_stats[week][player["id"]]["game"] + player["broken_tackles"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["dropped_passes"] = (player_stats[week][player["id"]]["dropped_passes"] * player_stats[week][player["id"]]["game"] + player["dropped_passes"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["catchable_passes"] = (player_stats[week][player["id"]]["catchable_passes"] * player_stats[week][player["id"]]["game"] + player["catchable_passes"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["yards_after_contact"] = (player_stats[week][player["id"]]["yards_after_contact"] * player_stats[week][player["id"]]["game"] + player["yards_after_contact"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["game"] += 1
                            if player["id"] in player_stats[week-1]:
                                player_stats[week-1][player["id"]]["weather"] = data["weather"]
                                player_stats[week-1][player["id"]]["opponent"] = away_id


                        if player["position"] == "WR":
                            home_stats["wr_first_downs"] += player["first_downs"]
                            home_stats["wr_receptions"] += player["receptions"]
                            home_stats["wr_targets"] += player["targets"]
                            home_stats["wr_yards"] += player["yards"]
                            home_stats["wr_avg_yards"] += player["avg_yards"]
                            home_stats["wr_longest"] += player["longest"]
                            home_stats["wr_touchdowns"] += player["touchdowns"]
                            home_stats["wr_yards_after_catch"] += player["yards_after_catch"]
                            home_stats["wr_redzone_targets"] += player["redzone_targets"]
                            home_stats["wr_air_yards"] += player["air_yards"]
                            home_stats["wr_broken_tackles"] += player["broken_tackles"]
                            home_stats["wr_dropped_passes"] += player["dropped_passes"]
                            home_stats["wr_catchable_passes"] += player["catchable_passes"]
                            home_stats["wr_yards_after_contact"] += player["yards_after_contact"]
                            wr_count += 1
                        elif player["position"] == "RB":
                            home_stats["rb_first_downs"] += player["first_downs"]
                            home_stats["rb_receptions"] += player["receptions"]
                            home_stats["rb_targets"] += player["targets"]
                            home_stats["rb_yards"] += player["yards"]
                            home_stats["rb_avg_yards"] += player["avg_yards"]
                            home_stats["rb_longest"] += player["longest"]
                            home_stats["rb_touchdowns"] += player["touchdowns"]
                            home_stats["rb_yards_after_catch"] += player["yards_after_catch"]
                            home_stats["rb_redzone_targets"] += player["redzone_targets"]
                            home_stats["rb_air_yards"] += player["air_yards"]
                            home_stats["rb_broken_tackles"] += player["broken_tackles"]
                            home_stats["rb_dropped_passes"] += player["dropped_passes"]
                            home_stats["rb_catchable_passes"] += player["catchable_passes"]
                            home_stats["rb_yards_after_contact"] += player["yards_after_contact"]
                            rb_count += 1
                        elif player["position"] == "TE":
                            home_stats["te_first_downs"] += player["first_downs"]
                            home_stats["te_receptions"] += player["receptions"]
                            home_stats["te_targets"] += player["targets"]
                            home_stats["te_yards"] += player["yards"]
                            home_stats["te_avg_yards"] += player["avg_yards"]
                            home_stats["te_longest"] += player["longest"]
                            home_stats["te_touchdowns"] += player["touchdowns"]
                            home_stats["te_yards_after_catch"] += player["yards_after_catch"]
                            home_stats["te_redzone_targets"] += player["redzone_targets"]
                            home_stats["te_air_yards"] += player["air_yards"]
                            home_stats["te_broken_tackles"] += player["broken_tackles"]
                            home_stats["te_dropped_passes"] += player["dropped_passes"]
                            home_stats["te_catchable_passes"] += player["catchable_passes"]
                            home_stats["te_yards_after_contact"] += player["yards_after_contact"]
                            te_count += 1

                    home_stats["wr_avg_yards"] = home_stats["wr_avg_yards"] / wr_count if wr_count > 0 else 0
                    home_stats["te_avg_yards"] = home_stats["te_avg_yards"] / te_count if te_count > 0 else 0
                    home_stats["rb_avg_yards"] = home_stats["rb_avg_yards"] / rb_count if rb_count > 0 else 0
                    
                    wr_count = 0
                    te_count = 0
                    rb_count = 0
                    for player in away:
                        player_actual[week][player["id"]] = player
                        if not player["id"] in player_stats[week]: 
                            player_stats[week][player["id"]] = player
                            player_stats[week][player["id"]]["game"] = 1
                        else: 
                            player_stats[week][player["id"]]["first_downs"] = (player_stats[week][player["id"]]["first_downs"] * player_stats[week][player["id"]]["game"] + player["first_downs"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["receptions"] = (player_stats[week][player["id"]]["receptions"] * player_stats[week][player["id"]]["game"] + player["receptions"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["targets"] = (player_stats[week][player["id"]]["targets"] * player_stats[week][player["id"]]["game"] + player["targets"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["yards"] = (player_stats[week][player["id"]]["yards"] * player_stats[week][player["id"]]["game"] + player["yards"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["avg_yards"] = (player_stats[week][player["id"]]["avg_yards"] * player_stats[week][player["id"]]["game"] + player["avg_yards"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["longest"] = (player_stats[week][player["id"]]["longest"] * player_stats[week][player["id"]]["game"] + player["longest"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["touchdowns"] = (player_stats[week][player["id"]]["touchdowns"] * player_stats[week][player["id"]]["game"] + player["touchdowns"]) / (player_stats[week][player["id"]]["game"] + 1)
                            # player_stats[week][player["id"]]["longest_touchdown"] = (player_stats[week][player["id"]]["longest_touchdown"] * player_stats[week][player["id"]]["game"] + player["longest_touchdown"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["yards_after_catch"] = (player_stats[week][player["id"]]["yards_after_catch"] * player_stats[week][player["id"]]["game"] + player["yards_after_catch"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["redzone_targets"] = (player_stats[week][player["id"]]["redzone_targets"] * player_stats[week][player["id"]]["game"] + player["redzone_targets"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["air_yards"] = (player_stats[week][player["id"]]["air_yards"] * player_stats[week][player["id"]]["game"] + player["air_yards"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["broken_tackles"] = (player_stats[week][player["id"]]["broken_tackles"] * player_stats[week][player["id"]]["game"] + player["broken_tackles"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["dropped_passes"] = (player_stats[week][player["id"]]["dropped_passes"] * player_stats[week][player["id"]]["game"] + player["dropped_passes"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["catchable_passes"] = (player_stats[week][player["id"]]["catchable_passes"] * player_stats[week][player["id"]]["game"] + player["catchable_passes"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["yards_after_contact"] = (player_stats[week][player["id"]]["yards_after_contact"] * player_stats[week][player["id"]]["game"] + player["yards_after_contact"]) / (player_stats[week][player["id"]]["game"] + 1)
                            player_stats[week][player["id"]]["game"] += 1
                            if player["id"] in player_stats[week-1]:
                                player_stats[week-1][player["id"]]["weather"] = data["weather"]
                                player_stats[week-1][player["id"]]["opponent"] = home_id


                        if player["position"] == "WR":
                            away_stats["wr_first_downs"] += player["first_downs"]
                            away_stats["wr_receptions"] += player["receptions"]
                            away_stats["wr_targets"] += player["targets"]
                            away_stats["wr_yards"] += player["yards"]
                            away_stats["wr_avg_yards"] += player["avg_yards"]
                            away_stats["wr_longest"] += player["longest"]
                            away_stats["wr_touchdowns"] += player["touchdowns"]
                            away_stats["wr_yards_after_catch"] += player["yards_after_catch"]
                            away_stats["wr_redzone_targets"] += player["redzone_targets"]
                            away_stats["wr_air_yards"] += player["air_yards"]
                            away_stats["wr_broken_tackles"] += player["broken_tackles"]
                            away_stats["wr_dropped_passes"] += player["dropped_passes"]
                            away_stats["wr_catchable_passes"] += player["catchable_passes"]
                            away_stats["wr_yards_after_contact"] += player["yards_after_contact"]
                            wr_count += 1
                        elif player["position"] == "RB":
                            away_stats["rb_first_downs"] += player["first_downs"]
                            away_stats["rb_receptions"] += player["receptions"]
                            away_stats["rb_targets"] += player["targets"]
                            away_stats["rb_yards"] += player["yards"]
                            away_stats["rb_avg_yards"] += player["avg_yards"]
                            away_stats["rb_longest"] += player["longest"]
                            away_stats["rb_touchdowns"] += player["touchdowns"]
                            away_stats["rb_yards_after_catch"] += player["yards_after_catch"]
                            away_stats["rb_redzone_targets"] += player["redzone_targets"]
                            away_stats["rb_air_yards"] += player["air_yards"]
                            away_stats["rb_broken_tackles"] += player["broken_tackles"]
                            away_stats["rb_dropped_passes"] += player["dropped_passes"]
                            away_stats["rb_catchable_passes"] += player["catchable_passes"]
                            away_stats["rb_yards_after_contact"] += player["yards_after_contact"]
                            rb_count += 1
                        elif player["position"] == "TE":
                            away_stats["te_first_downs"] += player["first_downs"]
                            away_stats["te_receptions"] += player["receptions"]
                            away_stats["te_targets"] += player["targets"]
                            away_stats["te_yards"] += player["yards"]
                            away_stats["te_avg_yards"] += player["avg_yards"]
                            away_stats["te_longest"] += player["longest"]
                            away_stats["te_touchdowns"] += player["touchdowns"]
                            away_stats["te_yards_after_catch"] += player["yards_after_catch"]
                            away_stats["te_redzone_targets"] += player["redzone_targets"]
                            away_stats["te_air_yards"] += player["air_yards"]
                            away_stats["te_broken_tackles"] += player["broken_tackles"]
                            away_stats["te_dropped_passes"] += player["dropped_passes"]
                            away_stats["te_catchable_passes"] += player["catchable_passes"]
                            away_stats["te_yards_after_contact"] += player["yards_after_contact"]
                            te_count += 1
                    away_stats["wr_avg_yards"] = away_stats["wr_avg_yards"] / wr_count if wr_count > 0 else 0
                    away_stats["te_avg_yards"] = away_stats["te_avg_yards"] / te_count if te_count > 0 else 0
                    away_stats["rb_avg_yards"] = away_stats["rb_avg_yards"] / rb_count if rb_count > 0 else 0

                    for id in [home_id, away_id]:
                        stats = home_stats if id == home_id else away_stats
                        if not id in team_stats[week]:
                            team_stats[week][id] = stats
                            team_stats[week][id]["games"] = 1
                        else:
                            team_stats[week][id]["wr_first_downs"] = (team_stats[week][id]["wr_first_downs"] * team_stats[week][id]["games"] + stats["wr_first_downs"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_receptions"] = (team_stats[week][id]["wr_receptions"] * team_stats[week][id]["games"] + stats["wr_receptions"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_targets"] = (team_stats[week][id]["wr_targets"] * team_stats[week][id]["games"] + stats["wr_targets"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_yards"] = (team_stats[week][id]["wr_yards"] * team_stats[week][id]["games"] + stats["wr_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_avg_yards"] = (team_stats[week][id]["wr_avg_yards"] * team_stats[week][id]["games"] + stats["wr_avg_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_longest"] = (team_stats[week][id]["wr_longest"] * team_stats[week][id]["games"] + stats["wr_longest"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_touchdowns"] = (team_stats[week][id]["wr_touchdowns"] * team_stats[week][id]["games"] + stats["wr_touchdowns"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_yards_after_catch"] = (team_stats[week][id]["wr_yards_after_catch"] * team_stats[week][id]["games"] + stats["wr_yards_after_catch"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_redzone_targets"] = (team_stats[week][id]["wr_redzone_targets"] * team_stats[week][id]["games"] + stats["wr_redzone_targets"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_air_yards"] = (team_stats[week][id]["wr_air_yards"] * team_stats[week][id]["games"] + stats["wr_air_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_broken_tackles"] = (team_stats[week][id]["wr_broken_tackles"] * team_stats[week][id]["games"] + stats["wr_broken_tackles"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_dropped_passes"] = (team_stats[week][id]["wr_dropped_passes"] * team_stats[week][id]["games"] + stats["wr_dropped_passes"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_catchable_passes"] = (team_stats[week][id]["wr_catchable_passes"] * team_stats[week][id]["games"] + stats["wr_catchable_passes"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["wr_yards_after_contact"] = (team_stats[week][id]["wr_yards_after_contact"] * team_stats[week][id]["games"] + stats["wr_yards_after_contact"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_first_downs"] = (team_stats[week][id]["te_first_downs"] * team_stats[week][id]["games"] + stats["te_first_downs"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_receptions"] = (team_stats[week][id]["te_receptions"] * team_stats[week][id]["games"] + stats["te_receptions"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_targets"] = (team_stats[week][id]["te_targets"] * team_stats[week][id]["games"] + stats["te_targets"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_yards"] = (team_stats[week][id]["te_yards"] * team_stats[week][id]["games"] + stats["te_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_avg_yards"] = (team_stats[week][id]["te_avg_yards"] * team_stats[week][id]["games"] + stats["te_avg_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_longest"] = (team_stats[week][id]["te_longest"] * team_stats[week][id]["games"] + stats["te_longest"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_touchdowns"] = (team_stats[week][id]["te_touchdowns"] * team_stats[week][id]["games"] + stats["te_touchdowns"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_yards_after_catch"] = (team_stats[week][id]["te_yards_after_catch"] * team_stats[week][id]["games"] + stats["te_yards_after_catch"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_redzone_targets"] = (team_stats[week][id]["te_redzone_targets"] * team_stats[week][id]["games"] + stats["te_redzone_targets"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_air_yards"] = (team_stats[week][id]["te_air_yards"] * team_stats[week][id]["games"] + stats["te_air_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_broken_tackles"] = (team_stats[week][id]["te_broken_tackles"] * team_stats[week][id]["games"] + stats["te_broken_tackles"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_dropped_passes"] = (team_stats[week][id]["te_dropped_passes"] * team_stats[week][id]["games"] + stats["te_dropped_passes"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_catchable_passes"] = (team_stats[week][id]["te_catchable_passes"] * team_stats[week][id]["games"] + stats["te_catchable_passes"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["te_yards_after_contact"] = (team_stats[week][id]["te_yards_after_contact"] * team_stats[week][id]["games"] + stats["te_yards_after_contact"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_first_downs"] = (team_stats[week][id]["rb_first_downs"] * team_stats[week][id]["games"] + stats["rb_first_downs"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_receptions"] = (team_stats[week][id]["rb_receptions"] * team_stats[week][id]["games"] + stats["rb_receptions"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_targets"] = (team_stats[week][id]["rb_targets"] * team_stats[week][id]["games"] + stats["rb_targets"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_yards"] = (team_stats[week][id]["rb_yards"] * team_stats[week][id]["games"] + stats["rb_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_avg_yards"] = (team_stats[week][id]["rb_avg_yards"] * team_stats[week][id]["games"] + stats["rb_avg_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_longest"] = (team_stats[week][id]["rb_longest"] * team_stats[week][id]["games"] + stats["rb_longest"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_touchdowns"] = (team_stats[week][id]["rb_touchdowns"] * team_stats[week][id]["games"] + stats["rb_touchdowns"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_yards_after_catch"] = (team_stats[week][id]["rb_yards_after_catch"] * team_stats[week][id]["games"] + stats["rb_yards_after_catch"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_redzone_targets"] = (team_stats[week][id]["rb_redzone_targets"] * team_stats[week][id]["games"] + stats["rb_redzone_targets"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_air_yards"] = (team_stats[week][id]["rb_air_yards"] * team_stats[week][id]["games"] + stats["rb_air_yards"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_broken_tackles"] = (team_stats[week][id]["rb_broken_tackles"] * team_stats[week][id]["games"] + stats["rb_broken_tackles"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_dropped_passes"] = (team_stats[week][id]["rb_dropped_passes"] * team_stats[week][id]["games"] + stats["rb_dropped_passes"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_catchable_passes"] = (team_stats[week][id]["rb_catchable_passes"] * team_stats[week][id]["games"] + stats["rb_catchable_passes"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["rb_yards_after_contact"] = (team_stats[week][id]["rb_yards_after_contact"] * team_stats[week][id]["games"] + stats["rb_yards_after_contact"]) / (team_stats[week][id]["games"] + 1)
                            team_stats[week][id]["games"] += 1


                    # print(json.dumps(rushing_data, indent=4))
                    # print(json.dumps(receiving_data, indent=4))

                    # merged_stats = []

                    # # Iterate through the first list
                    # for dict1 in rushing_data:
                    #     id1 = dict1.get("id")
                        
                    #     # Search for the matching ID in the second list
                    #     for dict2 in receiving_data:
                    #         id2 = dict2.get("id")
                            
                    #         # If IDs match, combine the dictionaries
                    #         if id1 == id2:
                    #             print(id1)
                    #             merged_dict = {**dict1, **dict2}
                    #             merged_stats.append(merged_dict)
                    #             break
                    #     else:
                    #         # If no match was found, add the dictionary from the first list
                    #         merged_stats.append(dict1)

                    # # Add the dictionaries from the second list that do not have matches
                    # for dict2 in receiving_data:
                    #     id2 = dict2.get("id")
                    #     for merged_dict in merged_stats:
                    #         id1 = merged_dict.get("id")
                    #         if id1 == id2:
                    #             break
                    #     else:
                    #         merged_stats.append(dict2)

                    # print(json.dumps(merged_stats, indent=4))
                    

                    # for player in rushing_data:
                    #     if not player["id"] in player_stats[week]: 
                    #         player_stats[week]["id"] = player
                    #         player_stats[week]["id"]["game"] = 1
                    #     else:
                    #         continue


                            
                    counter += 1
            week += 1
    for idx, actual in enumerate(player_actual):
        if idx > 4 and idx < 16:
            week_data = {}
            week_data["week"] = idx + 1
            week_data["players_averages"] = player_stats[idx-1]
            week_data["teams"] = team_stats[idx - 1]
            week_data["players_actual"] = actual
            with open(f'../data/{year}_player_stats/week{idx+1}.json', 'w') as json_file:
                json.dump(week_data, json_file, indent=4)


