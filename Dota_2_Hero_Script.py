from os import name, stat
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np

max_hero_level = 30

base_attributes = {
    'Base agility': 'base_agi',
    'Base intelligence': 'base_int',
    'Base strength': 'base_str'
}

base_attribute_key_list = []
for key in base_attributes.keys():
    base_attribute_key_list.append(key)

attribute_gain = {
    'Agility gain':'agi_gain',
    'Intelligence gain':'int_gain',
    'Strength gain':'str_gain'
}

attribute_gain_list_key_list = []
for key in attribute_gain.keys():
    attribute_gain_list_key_list.append(key)

def query(): #general query function, will be expanded to support additional query functionality.
    thing_to_find = input('Looking for: ' ) #
    is_in_columns = search_columns(thing_to_find) #search the columns for whatever you're looking for. If not there, will return False. 
    done_searching = False #set up a control loop to keep searching while....
    while done_searching == False:
        if is_in_columns == False:  #if it's not one of the column names, 
            to_search_heroes = input('Would you like to search for a specific hero? y/n, n to return to column search. ') #prompt. 
            if to_search_heroes == 'n': #if n, 
                column_to_find = input('Searching for column named: ') #loop back to column search. 
                column_search_results = search_columns(column_to_find)
                if column_search_results != False: #if it's not empty, it will automatically print, so just need to...
                    done_searching = True #let the logic flow know. Otherwise, it will loop again. 
            if to_search_heroes == 'y': #if y,
                hero_to_find = input('Hero to find: ') #look for a hero name instead.
                is_hero_found = search_heroes(hero_to_find) #conduct the search and print the results. 
                if is_hero_found != False: #if hero name is found, 
                    done_searching = True #exit loop.
                else:
                    print('Hero name not found. Terminating script.') #otherwise quit the script. Can build a control loop to keep searching, but not necessary. 
            else:
                print('Invalid input.')

    return

def search_heroes(hero_to_find): #returns index for each hero, or false if name is not recognized. 
    hero_table = get_table() #get the table. 
    hero_table['hero_name'] = hero_table['hero_name'].apply(lambda x: str(x).replace(u'\xa0', u'')) #fix some formatting errors. 
    hero_names = hero_table['hero_name'] #isolate the column of interest. Will expand upon this as a queryable function. 
    found_hero = False #using this just to see if the hero was found. 
    hero_name_list = [] #create a list to store all the hero names. hero_name_list_index = hero row index.

    for i in range(hero_names.size): #for each name in the hero_names column, 
        current_hero_name = hero_names[i] #assign it to a current variable. 
        hero_name_list.append(current_hero_name)
        if current_hero_name == hero_to_find: #if it matches the name we're looking for.
            found_hero = True #and let the program know it was found.

    if hero_to_find in hero_name_list:
        return hero_name_list.index(hero_to_find)

    if found_hero == False: #if it wasn't found, 
        print(hero_to_find,'not found.')
        return False #return false.

def get_table(): #this pretty much lies at the core of query functionality. Call the function to open the document. 
    hero_table = pd.read_csv(r'C:\Users\mathew.roberts\Desktop\Test Python Code\Dota_2_Hero_Table.csv')  #import the csv of hero stats.
    return hero_table

hero_table = get_table() #global hero table. Will remove redundancies eventually

def search_columns(col_name): #returns index for the column name. 
    hero_table = get_table() #get the table
    table_columns = [] #create a list to store all the column names. table_columns index = column name index.
    for i in range(len(hero_table.columns)): #and for each item in the list of column names.
        current_column_name = hero_table.columns[i]
        table_columns.append(current_column_name) #add that column name to table_columns

    if col_name in table_columns:
        return table_columns.index(col_name)

    else:
        print('Column not found. Available columns: ')
        for i in range(len(table_columns)):
            print(table_columns[i])
            time.sleep(0.05)

        return False

def format_column(column_name, str_to_remove): #dead function, just used to remove the \xa0's, wihch I may just write in manually on a case by case basis. But I'd prefer a function. 
    hero_table = get_table()
    table_columns = []

    for i in range(len(hero_table.columns)):
        table_columns.append(hero_table.columns[i])

    column_to_format = hero_table[column_name]
    column_to_format.apply(lambda x: str(x).replace(str_to_remove, u''))

    return column_to_format

def get_all_hero_names(): #lists all hero names, returned in array format. 
    hero_table = get_table()
    hero_table['hero_name'] = hero_table['hero_name'].apply(lambda x: str(x).replace(u'\xa0', u'')) #fix some formatting errors. 
    hero_names = hero_table['hero_name'] #isolate the column of interest. Will expand upon this as a queryable function. 
    name_array = [] #create an array to store the column information. 

    for i in range(hero_names.size): #iterate through the entire column. 
        name_array.append(hero_names[i]) #append the value to the array.
    
    print(name_array) #print the array for verification purposes.

def get_hero_stat(hero_to_find): #returns the value contained in the stat cell.
    hero_table = get_table()
    hero_table['hero_name'] = hero_table['hero_name'].apply(lambda x: str(x).replace(u'\xa0', u'')) #fix some formatting errors. 
    hero_names = hero_table['hero_name'] #isolate the column of interest. Will expand upon this as a queryable function.
    
    hero_index = search_heroes(hero_to_find)
    stat_to_find = input('Please enter a stat to find: ')
    stat_index = search_columns(stat_to_find)
    hero_stat = hero_table.iat[hero_index, stat_index]

    return hero_stat

class hero: #might as well just put all hero information in a hero class, and allow comparison that way....
    '''hero class. will contain stats, preferred items, etc. '''
    def __init__(self, name, level, primary_attribute, base_attr, attr_gain, abilities, roles):
        self.name = name
        self.level = level
        self.primary_attribute = primary_attribute
        self.base_attr = base_attr
        self.attr_gain = attr_gain
        self.abilities = abilities #will append abilities somehow...
        self.roles = roles #not currently useful, will be used for idea prototyping.

    def set_name(): #sets the hero name
        name = input('Please enter hero name: ') #get the hero name. Will be expanded upon to include verification and 'like' similarity suggestions.
        return name

    name = set_name()

    def set_level(x): #create a function for manually adjusting levels. 
        level = x
        return level

    level = set_level(0)

    def set_primary_attribute(name): #dynamically retrieve the primary attribute. 
        hero_table = get_table() #get the table
        hero_index = search_heroes(name) #get the hero index 
        primary_attribute_index = search_columns('primary_attribute') #then the primary attribute index.
        primary_attribute = hero_table.iat[hero_index, primary_attribute_index] #then find the exact value using the two indices. 
        return primary_attribute #return that value.

    primary_attribute = set_primary_attribute(name)

    def set_base_attributes(name): #dynamiclly set the base attributes. 
        hero_table = get_table()
        hero_index = search_heroes(name)
        base_attr_dict = {}
        i = 0
        for base_attr_key in base_attributes:
            current_base_index = search_columns(base_attributes[base_attr_key])
            current_base_attr = hero_table.iat[hero_index, current_base_index]
            base_attr_dict[base_attribute_key_list[i]] = current_base_attr
            i += 1

        return base_attr_dict

    base_attr = set_base_attributes(name)

    def set_attr_gain(name): #dynamically initialize the attribute gain for each hero. 
        hero_table = get_table() #get the table. 
        hero_index = search_heroes(name) #get the hero name index.
        attr_gain_dict = {} #create dictionary to hold values. 
        i = 0
        for attr_gain_key in attribute_gain: #and for each attribute gain we're looking to find
            current_attr_index = search_columns(attribute_gain[attr_gain_key]) #get the index for that column
            current_attr_gain = hero_table.iat[hero_index, current_attr_index] #and find the value in that cell w/ the hero.
            attr_gain_dict[attribute_gain_list_key_list[i]] = current_attr_gain #write that value into the attr gain list. 
            i+=1
        
        return attr_gain_dict

    attr_gain = set_attr_gain(name)

    def plot_hero_stat_gain(hero_name): #plot hero stats vs level
        hero_index = search_heroes(hero_name)
        level_list = list(range(0,31))
        
        def get_agi_gain():
            base_agi = hero_table.iat[hero_index,search_columns('base_agi')]
            agi_gain = hero_table.iat[hero_index,search_columns('agi_gain')]
            agi_gain_list = []
            for i in level_list:
                current_agi = base_agi + agi_gain * i
                agi_gain_list.append(current_agi)
            
            return agi_gain_list

        def get_int_gain():
            base_int = hero_table.iat[hero_index, search_columns('base_int')]
            int_gain = hero_table.iat[hero_index, search_columns('int_gain')]
            int_gain_list = []
            for i in level_list:
                current_int = base_int + int_gain * i
                int_gain_list.append(current_int)
            
            return int_gain_list

        def get_str_gain():
            base_str = hero_table.iat[hero_index, search_columns('base_str')]
            str_gain = hero_table.iat[hero_index, search_columns('str_gain')]
            str_gain_list = []
            for i in level_list:
                current_str = base_str + str_gain * i
                str_gain_list.append(current_str)

            return str_gain_list

        agi_gain_list = get_agi_gain()
        int_gain_list = get_int_gain()
        str_gain_list = get_str_gain()

        plt.plot(level_list, agi_gain_list, 'g^',
                    level_list, int_gain_list, 'bs',
                    level_list, str_gain_list, 'r--')
        plt.xlabel('Level')
        plt.ylabel('Stat Quantity')
        stat_gain = ' stat gain'
        plot_title = hero_name + stat_gain
        plt.title(plot_title)
        plt.show()

new_hero = hero
new_hero.plot_hero_stat_gain(new_hero.name)
