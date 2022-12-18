# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 18:58:40 2022

@author: lukas & anders
"""

#%% Sound
def play_sound():
    #Play sound. Used when calculations finish.
    import winsound
    import time
    winsound.Beep(294, 800)
    winsound.Beep(311, 300)
    winsound.Beep(233, 800)
    
#%% Get country Data
def get_load_and_price(year): # require year
    import pandas as pd
        
    cprice = pd.read_csv("Data/market/price_%d.csv"%year, index_col = 0)
    cload = pd.read_csv("Data/market/load_%d.csv"%year, index_col = 0)
    # cprice = 1
    # cload = 1
    
    
    return cprice, cload

#%% Annuity
def get_annuity(i, n):
    annuity = i/(1.-1./(1.+i)**n)
    return annuity

#%% Remove outliers
def remove_outliers(df,columns,n_std):
    for col in columns:
        print('Working on column: {}'.format(col))
        
        mean = df[col].mean()
        sd = df[col].std()
        
        df = df[(df[col] <= mean+(n_std*sd))]
        
    return df

def earth_distance(lat1,lat2,lon1,lon2):
    import numpy as np
    R = 6378.1  #Earths radius
    dlon = (lon2 - lon1) * np.pi/180
    dlat = (lat2 - lat1) * np.pi/180
    
    lat1 = lat1 * np.pi/180
    lat2 = lat2 * np.pi/180
    
    a = (np.sin(dlat/2))**2 + np.cos(lat1) * np.cos(lat2) * (np.sin(dlon/2))**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a)) 
    d = R*c #Spherical distance between two points
    
    return d