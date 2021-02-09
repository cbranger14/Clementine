import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import glob
import os
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


df = pd.DataFrame(columns = ['startTime', 'stopTime', 'timezoneOffset', 'duration', 'distance',
       'sport', 'latitude', 'longitude', 'ascent', 'descent', 'kiloCalories',
       'heartRate', 'speed', 'cadence', 'zones', 'laps', 'autoLaps', 'samples',
       'target'])
def load_file(filename):
    global df
    with open(filename,'r') as a:
        session =json.loads(a.read())
        df_session = pd.DataFrame(session["exercises"])
        df= df.append(df_session, ignore_index=True)
        df.index += 1
        
    
load_file('training-session1.json')
load_file('training-session2.json')
load_file('training-session3.json') 
load_file('training-session4.json')
load_file('training-session5.json')
load_file('training-session6.json')
load_file('training-session7.json')
load_file('training-session8.json')
load_file('training-session9.json')
load_file('training-session10.json')
load_file('training-session11.json')
load_file('training-session12.json')
load_file('training-session13.json')
load_file('training-session14.json')
load_file('training-session15.json')
load_file('training-session16.json')
load_file('training-session17.json')
load_file('training-session18.json')
load_file('training-session19.json')
load_file('training-session20.json')
load_file('training-session21.json')
load_file('training-session22.json')
load_file('training-session23.json')
load_file('training-session24.json')
load_file('training-session25.json')
load_file('training-session26.json')
load_file('training-session27.json')
load_file('training-session28.json')
load_file('training-session29.json')
load_file('training-session30.json')
load_file('training-session31.json')
load_file('training-session32.json')
load_file('training-session33.json')
load_file('training-session34.json')
load_file('training-session35.json')
load_file('training-session36.json')
load_file('training-session37.json')
load_file('training-session38.json')
load_file('training-session39.json')
load_file('training-session40.json')
load_file('training-session41.json')
load_file('training-session42.json')
load_file('training-session43.json')
load_file('training-session44.json')
load_file('training-session45.json')
load_file('training-session46.json')
load_file('training-session47.json')
load_file('training-session48.json')
load_file('training-session49.json')
load_file('training-session50.json')
load_file('training-session51.json')
load_file('training-session52.json')
load_file('training-session53.json')
load_file('training-session54.json')
load_file('training-session55.json')
load_file('training-session56.json')
load_file('training-session57.json')
load_file('training-session58.json')
load_file('training-session59.json')
load_file('training-session60.json')
load_file('training-session61.json')
load_file('training-session62.json')
load_file('training-session63.json')
load_file('training-session64.json')
load_file('training-session65.json')
load_file('training-session66.json')
load_file('training-session67.json')
load_file('training-session68.json')
load_file('training-session69.json')
load_file('training-session70.json')
load_file('training-session71.json')
load_file('training-session72.json')
load_file('training-session73.json')
load_file('training-session74.json')
load_file('training-session75.json')
load_file('training-session76.json')
load_file('training-session77.json')
load_file('training-session79.json')
load_file('training-session80.json')
load_file('training-session81.json')
load_file('training-session82.json')
load_file('training-session83.json')
load_file('training-session84.json')
load_file('training-session85.json')
load_file('training-session86.json')
load_file('training-session87.json')
load_file('training-session88.json')

# print(df)

df = df.drop(columns= ['timezoneOffset','latitude', 'longitude', 'ascent','descent', 'samples', 'target'])
df = df.drop(df[df.sport != "RUNNING"].index)
print(df.describe())





