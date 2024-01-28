import numpy as np
import json

with open('../data/2022_Stats.json', 'r') as file:
    data = json.load(file)

stats = [(player['averages']['yards'], player['defense']['position_yards'], player['averages']['position'], player['averages']['targets'], player['averages']['avg_yards'], player['defense']['position_avg_yards'], player['averages']['redzone_targets'], idx) for idx, player in enumerate(data)]

thresholds = [
    np.percentile([yard for yard, _, _, _, _, _, _, _ in stats], 95),
    np.percentile([yard for yard, _, _, _, _, _, _, _ in stats], 75),
    np.percentile([yard for yard, _, _, _, _, _, _, _ in stats], 30),
    np.percentile([yard for yard, _, _, _, _, _, _, _ in stats], 15)
]

offensive_yards = {
    'Elite': [],
    'Good': [],
    'Average': [],
    'Ok': [],
    'Poor': []
}

for yard, _, _, _, _, _, _, idx in stats:
    if yard >= thresholds[0]:
        offensive_yards['Elite'].append((yard, idx))
    elif yard >= thresholds[1]:
        offensive_yards['Good'].append((yard, idx))
    elif yard >= thresholds[2]:
        offensive_yards['Average'].append((yard, idx))
    elif yard >= thresholds[3]:
        offensive_yards['Ok'].append((yard, idx))
    else:
        offensive_yards['Poor'].append((yard, idx))

offensive_yards_stats = {}

for category, yards in offensive_yards.items():
    category_yards = [yard for yard, _ in yards] 
    mean = np.mean(category_yards)
    std = np.std(category_yards) 
    offensive_yards_stats[category] = {'Mean': mean, 'Standard_Deviation': std}

#offensive yards per catch
thresholds = [
    np.percentile([yards_per_catch for _, _, _, yards_per_catch, _, _, _, _ in stats], 90),
    np.percentile([yards_per_catch for _, _, _, yards_per_catch, _, _, _, _ in stats], 50),
]

offensive_yards_per_catch = {
    'High': [],
    'Medium': [],
    'Low': [],
}

for _, _, _, _, yards_per_catch, _, _, idx in stats:
    if yards_per_catch >= thresholds[0]:
        offensive_yards_per_catch['High'].append((yards_per_catch, idx))
    elif yards_per_catch >= thresholds[1]:
        offensive_yards_per_catch['Medium'].append((yards_per_catch, idx))
    else:
        offensive_yards_per_catch['Low'].append((yards_per_catch, idx))

offensive_yards_per_catch_stats = {}

for category, yards_per_catch in offensive_yards_per_catch.items():
    category_yards_per_catch = [target for target, _ in yards_per_catch] 
    mean = np.mean(category_yards_per_catch)
    std = np.std(category_yards_per_catch) 
    offensive_yards_per_catch_stats[category] = {'Mean': mean, 'Standard_Deviation': std}


#offensive targets
thresholds = [
    np.percentile([targets for _, _, _, targets, _, _, _, _ in stats], 90),
    np.percentile([targets for _, _, _, targets, _, _, _, _ in stats], 70),
    np.percentile([targets for _, _, _, targets, _, _, _, _ in stats], 50),
    np.percentile([targets for _, _, _, targets, _, _, _, _ in stats], 25)
]

offensive_targets = {
    'Elite': [],
    'Good': [],
    'Average': [],
    'Ok': [],
    'Poor': []
}

for _, _, _, targets, _, _, _, idx in stats:
    if targets >= thresholds[0]:
        offensive_targets['Elite'].append((targets, idx))
    elif targets >= thresholds[1]:
        offensive_targets['Good'].append((targets, idx))
    elif targets >= thresholds[2]:
        offensive_targets['Average'].append((targets, idx))
    elif targets >= thresholds[3]:
        offensive_targets['Ok'].append((targets, idx))
    else:
        offensive_targets['Poor'].append((targets, idx))

offensive_targets_stats = {}

for category, targets in offensive_targets.items():
    category_targets = [target for target, _ in targets] 
    mean = np.mean(category_targets)
    std = np.std(category_targets) 
    offensive_targets_stats[category] = {'Mean': mean, 'Standard_Deviation': std}



#defensive yards 
position_thresholds = {}
for position_filter in ["WR", "TE", "RB"]:
    position_thresholds[position_filter] = [
        np.percentile([yard for _, yard, position, _, _, _, _, _ in stats if position == position_filter], 90),
        np.percentile([yard for _, yard, position, _, _, _, _, _ in stats if position == position_filter], 70),
        np.percentile([yard for _, yard, position, _, _, _, _, _ in stats if position == position_filter], 50),
        np.percentile([yard for _, yard, position, _, _, _, _, _ in stats if position == position_filter], 25)
    ]

defensive_yards = {
    'WR': {'Elite': [], 'Good': [], 'Average': [], 'Ok': [], 'Poor': []},
    'TE': {'Elite': [], 'Good': [], 'Average': [], 'Ok': [], 'Poor': []},
    'RB': {'Elite': [], 'Good': [], 'Average': [], 'Ok': [], 'Poor': []}
}

for _, yard, position, _, _, _, _, idx in stats:
    thresholds = position_thresholds[position]
    category = None
    if yard >= thresholds[0]:
        category = 'Elite'
    elif yard >= thresholds[1]:
        category = 'Good'
    elif yard >= thresholds[2]:
        category = 'Average'
    elif yard >= thresholds[3]:
        category = 'Ok'
    else:
        category = 'Poor'
    defensive_yards[position][category].append((yard, idx))

defensive_yards_stats = {position: {} for position in defensive_yards}

for position, categories in defensive_yards.items():
    for category, yards in categories.items():
        category_yards = [yard for yard, _ in yards]
        mean = np.mean(category_yards)
        std = np.std(category_yards)
        defensive_yards_stats[position][category] = {'Mean': mean, 'Standard_Deviation': std}

#offsensive red zone targets
thresholds = [
    np.percentile([red_zone_targets for _, _, _, _, _, _, red_zone_targets, _ in stats], 90),
    np.percentile([red_zone_targets for _, _, _, _, _, _, red_zone_targets, _ in stats], 50),
]

print(thresholds)

offensive_red_zone_targets = {
    'Elite': [],
    'Average': [],
    'Poor': []
}

for _, _, _, _, _, _, red_zone_target, idx in stats:
    if red_zone_target >= thresholds[0]:
        offensive_red_zone_targets['Elite'].append((red_zone_target, idx))
    elif red_zone_target >= thresholds[1]:
        offensive_red_zone_targets['Average'].append((red_zone_target, idx))
    else:
        offensive_red_zone_targets['Poor'].append((red_zone_target, idx))

offensive_red_zone_targets_stats = {}

for category, red_zone_targets in offensive_red_zone_targets.items():
    category_red_zone_targets = [red_zone_target for red_zone_target, _ in red_zone_targets] 
    mean = np.mean(category_red_zone_targets)
    std = np.std(category_red_zone_targets) 
    offensive_red_zone_targets_stats[category] = {'Mean': mean, 'Standard_Deviation': std}



#defense yards per reception
position_thresholds = {}
for position_filter in ["WR", "TE", "RB"]:
    position_thresholds[position_filter] = [
        np.percentile([yards_per_catch for _, _, position, _, _, yards_per_catch, _, _ in stats if position == position_filter], 90),
        np.percentile([yards_per_catch for _, _, position, _, _, yards_per_catch, _, _ in stats if position == position_filter], 50),
       
    ]

defensive_yards_per_catch = {
    'WR': {'High': [], 'Medium': [], 'Low': []},
    'TE': {'High': [], 'Medium': [], 'Low': []},
    'RB': {'High': [], 'Medium': [], 'Low': []}
}

for _, _, position, _, _, yards_per_catch, _, idx in stats:
    thresholds = position_thresholds[position]
    category = None
    if yards_per_catch >= thresholds[0]:
        category = 'High'
    elif yards_per_catch >= thresholds[1]:
        category = 'Medium'
    else:
        category = 'Low'
    defensive_yards_per_catch[position][category].append((yards_per_catch, idx))

defensive_yards_per_catch_stats = {position: {} for position in defensive_yards_per_catch}

for position, categories in defensive_yards_per_catch.items():
    for category, yards in categories.items():
        category_yards = [yard for yard, _ in yards]
        mean = np.mean(category_yards)
        std = np.std(category_yards)
        defensive_yards_per_catch_stats[position][category] = {'Mean': mean, 'Standard_Deviation': std}

data_object = {
    "average_yards" : offensive_yards_stats,
    "average_targets": offensive_targets_stats,
    "average_yards_per_catch": offensive_yards_per_catch_stats,
    "red_zone_targets": offensive_red_zone_targets_stats,
    "defense_yards_per_catch": defensive_yards_per_catch_stats,
    "defensive_average_yards": defensive_yards_stats
}
with open(f'../data/stats.json', 'w') as json_file:
        json.dump(data_object, json_file, indent=4)
    
    