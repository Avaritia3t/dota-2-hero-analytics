import json

heroStatsFilePath = r'C:\Users\Sol\Desktop\allPythonCode\hero-stats'

enemyPickOne = None
enemyPickTwo = None
enemyPickThree = None
enemyPickFour = None
enemyPick5 = None


def draft():
    # Code to suggest picks for a DotA 2 draft.
    
    def getFirstPicks():
        # Open the JSON file with hero stats
        with open(heroStatsFilePath, 'r') as f:
            hero_stats = json.load(f)
    
        # Initialize an empty list to store the picks
        pick_ids = []
    
        # Iterate through the hero stats and check for the desired conditions
        for key, value in hero_stats.items():
            if 'Support' in value['roles']:
                if value['base_armor'] >=3 or value['base_health_regen'] > 5:
                    print(value['localized_name'])
                    pick_ids.append(value['id'])
                else:
                    pass

        print(pick_ids)
        return
    
    def getSecondPicks():
        pass
        return

    def getThirdPicks():
        pass
        return
    

    while enemyPickOne == None:
        getFirstPicks()
        
    firstRoundPicks = getFirstPicks()
    secondRoundPicks = getSecondPicks()
    thirdRoundPicks = getThirdPicks()

    player_name = input()
    # etc.

draft = draft

def itemize():
    # Code to itemize players
    print("Enter the name of the player you want to itemize:")
    player_name = input()
    # etc.

itemize = itemize

def analyze():
    # Code to analyze players
    print("Enter the name of the player you want to analyze:")
    player_name = input()
    # etc.

analyze = analyze


def query_hero():
    # Prompt the user for input
    name = input("Enter the name of the hero: ")

    # Open the JSON file
    with open(heroStatsFilePath, 'r') as f:
        heroes = json.load(f)

    # Find the appropriate entry in the JSON data
    for hero in heroes.values():
        if hero['localized_name'] == name:
            hero_stats = hero
            break
    else:
        # Return None if the hero was not found
        return None

    # Return the hero stats
    return hero_stats

#hero_data = query_hero()
#print(json.dumps(hero_data, indent=4, sort_keys=True))

def get_action():
    # Dictionary of valid inputs
    valid_input = {
    "draft": draft,
    "itemize": itemize,
    "analyze": analyze,
}

    
    # Prompt the user for input
    user_input = input("What would you like to do? ")

    # Check if the input is in the dictionary
    if user_input in valid_input:
        # Call the corresponding function
        valid_input[user_input]()
    else:
        # Input is not recognized, prompt the user again
        print("Sorry, I didn't understand that command.")
        get_action()

draft()