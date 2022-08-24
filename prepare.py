# import essential libraries
import pandas as pd
import numpy as np

# import local acquire file
import acquire

def prep_data(df):
    '''
    This function takes in a messy dataframe and return the cleaned verison of dataframe.
    Detial steps are in code comment below.
    '''
    # Set date columns as datatime as index
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date)

    # Drop null values
    df = df.dropna()

    # Encode program_id
    df['program'] = df.program_id.map({1: 'Full Stack PHP', 2: 'Full Stack Java', 3: 'Data Science', 4: 'Front End'})

    return df