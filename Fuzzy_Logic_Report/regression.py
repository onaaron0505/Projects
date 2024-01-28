import math
import random
import numpy as np
import json
from mamdani import Mamdani, Rule

def gaussian(x, mu, sigma):
    exponential = -(x - mu)**2 / (2 * sigma**2)
    return math.exp(exponential)

def points(player):
    return player['actual']['touchdowns'] * 6 + player['actual']['receptions'] + player['actual']['yards'] * 0.1

with open('./data/2022_Stats.json', 'r') as file:
    data = json.load(file)

with open('./data/2023_player_stats/week9.json', 'r') as file:
    data2023 = json.load(file)

with open('./data/stats.json', 'r') as file:
    stats = json.load(file)


#actual data
combinations = {}
for avg_cat, avg_stats in stats['average_yards'].items():
    combinations[avg_cat] = {}
    for position, def_cats in stats['defensive_average_yards'].items():
        for def_cat, def_stats in def_cats.items():
            combinations[avg_cat][def_cat] = []
            
for player in data:
    yards = player['averages']['yards']
    defensive_yards = player['defense']['position_yards']
    for avg_cat, avg_stats in stats['average_yards'].items():
        mean_avg_yards = avg_stats['Mean']
        std_avg_yards = avg_stats['Standard_Deviation']
        
        for position, def_cats in stats['defensive_average_yards'].items():
            for def_cat, def_stats in def_cats.items():
                mean_def_yards = def_stats['Mean']
                std_def_yards = def_stats['Standard_Deviation']
                offense = random.random()
                defense = random.random()
                gaussian_offense = gaussian(yards, mean_avg_yards, std_avg_yards)
                gaussian_defense = gaussian(defensive_yards, mean_def_yards, std_def_yards)
                if  (gaussian_offense >= offense and gaussian_defense >= defense) or (avg_cat == 'Elite' and (player['averages']['yards'] >= mean_avg_yards)) :
                    combinations[avg_cat][def_cat].append(points(player))

stats_results = {avg_cat: {} for avg_cat in combinations}

for avg_cat in combinations:
    for def_cat in combinations[avg_cat]:
        points_list = combinations[avg_cat][def_cat]
        if points_list:
            avg_points = np.mean(points_list)
            std_dev_points = np.std(points_list)
        else:
            avg_points = None
            std_dev_points = None
        
        stats_results[avg_cat][def_cat] = {
            'Average': avg_points,
            'Standard_Deviation': std_dev_points
        }



rules = []


for avg_cat in stats_results:
    for def_cat in stats_results[avg_cat]:
        rule = Rule()   
        rule.add_gaussian_antecedent("Yards", avg_cat, stats['average_yards'][avg_cat]['Mean'], stats['average_yards'][avg_cat]['Standard_Deviation'])
        rule.add_gaussian_antecedent("Defense_Yards", def_cat, stats['defensive_average_yards']['WR'][def_cat]['Mean'], stats['defensive_average_yards']['WR'][def_cat]['Standard_Deviation'])

        rule.add_gaussian_consequent("Points", avg_cat + ' ' + def_cat, stats_results[avg_cat][def_cat]['Average'], stats_results[avg_cat][def_cat]['Standard_Deviation'])

        rules.append(rule)

fis = Mamdani(rules, [0, 70])

player_id = 'fa99e984-d63b-4ef4-a164-407f68a7eeaf'
yards =  data2023['players_averages'][player_id]['yards']
# defensive_yards = data2023['teams'][data2023['players_averages'][player_id]['opponent']]['wr_yards']
defensive_yards = data2023['teams']['768c92aa-75ff-4a43-bcc0-f2798c2e1724']['wr_yards']

inputs = [{"name": "Yards", "value": yards}, {"name": "Defense_Yards", "value": defensive_yards}]

print(fis.make_inference(inputs))


