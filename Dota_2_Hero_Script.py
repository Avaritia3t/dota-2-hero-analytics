import pandas as pd
import time

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

def search_heroes(hero_to_find): #function to return specific hero row from the list. 
    hero_table = get_table() #get the table. 
    hero_table['hero_name'] = hero_table['hero_name'].apply(lambda x: str(x).replace(u'\xa0', u'')) #fix some formatting errors. 
    hero_names = hero_table['hero_name'] #isolate the column of interest. Will expand upon this as a queryable function. 
    found_hero = False #using this just to see if the hero was found. 

    for i in range(hero_names.size): #for each name in the hero_names column, 
        current_hero_name = hero_names[i] #assign it to a current variable. 
        if current_hero_name == hero_to_find: #if it matches the name we're looking for. 
            print(hero_table.iloc[[i]]) #print the associated row. 
            found_hero = True #and let the program know it was found. 

    if found_hero == False: #if it wasn't found, 
        return False #return false.


def get_table(): #this pretty much lies at the core of query functionality. Call the function to open the document. 
    hero_table = pd.read_csv(r'C:\Users\mathew.roberts\Desktop\Test Python Code\Dota_2_Hero_Table.csv')  #import the csv of hero stats.
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
