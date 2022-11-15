import pandas as pd
import warnings
import calendar
# import numpy as np
warnings.filterwarnings("ignore")

import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:hogl1234@104.198.131.115/CedricBox')

def update_db(up_data):

    df = pd.read_csv(up_data)
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    df['Time'] = pd.to_datetime(df['Time']).dt.time

    df.to_sql('cedric_box_data', engine, if_exists = 'append', index = False)

    return "Updated Successfully!"

