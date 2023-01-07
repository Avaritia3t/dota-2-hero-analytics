import json

heroStatsFilePath = r'C:\Users\Sol\Desktop\allPythonCode\hero-stats'

with open(heroStatsFilePath, 'r') as f:
    heroes = json.load(f)

    print(heroes)