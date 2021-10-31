#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error

# data preparation

dataAir = 'aqi_yearly_1980_to_2021.csv'
usecols = ['State', 'County', 'Year', 'Days with AQI', 'Good Days', 'Moderate Days', 
           'Unhealthy for Sensitive Groups Days', 'Unhealthy Days', 'Very Unhealthy Days', 'Hazardous Days',
           'Median AQI', 'Days CO', 'Days NO2', 'Days Ozone', 'Days SO2',
           'Days PM2.5', 'Days PM10', 'Latitude', 'Longitude']
dfAir = pd.read_csv(dataAir, usecols=usecols)

dfAir = dfAir[(dfAir['Year']==2016)]
del dfAir['Year']
dfAir.columns = dfAir.columns.str.lower().str.replace(' ', '_')
strings = list(dfAir.dtypes[dfAir.dtypes == 'object'].index)
for col in strings:
    dfAir[col] = dfAir[col].str.lower().str.strip().str.replace(' ', '_')
usecols = ['StateDesc', 'CountyName', 'TotalPopulation', 'CASTHMA_AdjPrev']
dataAsthma = 'PLACES_County_Data.csv'
dfAsthma = pd.read_csv(dataAsthma, usecols=usecols)

dfAsthma.columns = dfAsthma.columns.str.lower().str.replace(' ', '_')
strings = list(dfAsthma.dtypes[dfAsthma.dtypes == 'object'].index)
for col in strings:
    dfAsthma[col] = dfAsthma[col].str.lower().str.replace(' ', '_')
dfAsthma = dfAsthma.rename(columns={"countyname": "county", "statedesc": "state"})
df = pd.merge(dfAir, dfAsthma, left_on=['state','county'], right_on = ['state','county'], how='inner')

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = np.log1p(df_train.casthma_adjprev.values)
y_val = np.log1p(df_val.casthma_adjprev.values)
y_test = np.log1p(df_test.casthma_adjprev.values)

del df_train['casthma_adjprev']
del df_val['casthma_adjprev']
del df_test['casthma_adjprev']

train_dicts = df_train.to_dict(orient='records')
val_dicts = df_val.to_dict(orient='records')

dv = DictVectorizer(sparse=False)

X_train = dv.fit_transform(train_dicts)
X_val = dv.transform(val_dicts)

fr = RandomForestRegressor(n_estimators=200, max_depth=45, 
                           random_state=1, n_jobs=-1)
fr.fit(X_train, y_train)
y_pred = fr.predict(X_val)
score = np.sqrt(mean_squared_error(y_val, y_pred))
print('score:')
print(score)

model_file = 'model1.bin'
dv_file = 'dv1.bin'

with open(model_file, 'wb') as f_out: 
    pickle.dump((fr), f_out)

with open(dv_file, 'wb') as f_out: 
    pickle.dump((dv), f_out)

print(f'the model is saved to {model_file}')
