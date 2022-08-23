import pandas as pd
import os
import env

# Getting conncection to mySQL database, and acquiring data
def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
    This function gets conncection to mySQL database
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# Loading raw data from Curriculum_Log database
def new_data():
    '''
    This function reads the curriculum data from the mySQL database into a df.
    '''
    # Create SQL query.
    sql_query = '''
    SELECT * FROM logs LEFT JOIN cohorts ON logs.user_id = cohorts.id
    '''
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('curriculum_logs'))
    
    return df

def get_data():
    '''
    This function reads in curriculum data from curriculum_log database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('curriculum.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('curriculum.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = new_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('curriculum.csv')
        
    return df