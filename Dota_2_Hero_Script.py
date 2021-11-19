import pandas as pd
import time

def query(): #general query function, will be expanded to support additional query functionality.
    thing_to_find = input('Looking for: ' ) #
    is_in_columns = search_columns(thing_to_find)
    done_searching = False
    while done_searching == False:
        if is_in_columns == False: 
            to_search_heroes = input('Would you like to search for a specific hero? y/n, n to return to column search. ')
            if to_search_heroes == 'n':
                column_to_find = input('Searching for column named: ')
                search_columns(column_to_find)
                if search_columns != False:
                    done_searching = True
                    return
            if to_search_heroes == 'y':
                hero_to_find = input('Hero to find: ')
                is_hero_found = search_heroes(hero_to_find)
                if is_hero_found != False:
                    done_searching = True
                    return
            else:
                print('Invalid input.')

def search_heroes(hero_to_find):
    hero_table = get_table()
    hero_table['hero_name'] = hero_table['hero_name'].apply(lambda x: str(x).replace(u'\xa0', u'')) #fix some formatting errors. 
    hero_names = hero_table['hero_name'] #isolate the column of interest. Will expand upon this as a queryable function. 

    for i in range(hero_names.size):
        if hero_names[i] == hero_to_find:
            pass

def get_table(): #this pretty much lies at the core of query functionality. Call the function to open the document. 
    hero_table = pd.read_csv(r'C:\Users\19512\Desktop\Python Code\Dota_2_Hero_Table.csv')  #import the csv of hero stats.
    return hero_table

def search_columns(col_name): #initially, will analyze by column. 
    hero_table = get_table() #get the table
    table_columns = [] #create a list to store all the column names. table_columns index = column name index.
    for i in range(len(hero_table.columns)): #and for each item in the list of column names. 
        current_column_name = hero_table.columns[i]
        table_columns.append(current_column_name) #add that column name to table_columns

    if col_name in table_columns:
        print(hero_table[col_name])
        return True
    else:
        print('Column not found.')
        for i in range(len(table_columns)):
            print(table_columns[i])
            time.sleep(0.05)

        return False

def format_column():
    hero_table = get_table()
    table_columns = []

    for i in range(len(hero_table.columns)):
        table_columns.append(hero_table.columns[i])

    column_to_format = input('Which column would you like to format?')

def get_all_hero_names():
    hero_table = get_table()
    hero_table['hero_name'] = hero_table['hero_name'].apply(lambda x: str(x).replace(u'\xa0', u'')) #fix some formatting errors. 
    hero_names = hero_table['hero_name'] #isolate the column of interest. Will expand upon this as a queryable function. 
    name_array = [] #create an array to store the column information. 

    for i in range(hero_names.size): #iterate through the entire column. 
        name_array.append(hero_names[i]) #append the value to the array.
    
    print(name_array) #print the array for verification purposes.

def get_hero_stats():
    hero_table = get_table()
    hero_table['hero_name'] = hero_table['hero_name'].apply(lambda x: str(x).replace(u'\xa0', u'')) #fix some formatting errors. 
    hero_names = hero_table['hero_name'] #isolate the column of interest. Will expand upon this as a queryable function. 

search_heroes('Axe')