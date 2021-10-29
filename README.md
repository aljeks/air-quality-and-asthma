# air-quality-and-asthma

### Problem description

This ML project is model of air quality data with prediction of asthma prevalence for some region.
It's based on data for all counties of USA.
My assamption is an air quality index for any city is correlated with quantity of people that have Asthma disease.

Solution of this problem can help people to choose correct place to live, espessially if they have Asthma.
Any person can see what features of the city is the most important to avoid asthma.
Avoiding 'bad' areas can help to improve your health.

### What data I use

Two datasets are merged in this project "Air Quality" and "Asthma prevalence"

The 1st dataset is "1980-2021 Yearly Air Quality Index from the US Environmental Protection Agency" 
https://www.kaggle.com/threnjen/40-years-of-air-quality-index-from-the-epa-yearly

This set includes yearly reports of air quality index (AQI) from various US Metro areas, as well as geographic data for the collection locations.
Data includes this columns:
'State', 'County', 'Year', 
'Days with AQI', 'Good Days', 'Moderate Days', 
'Unhealthy for Sensitive Groups Days', 'Unhealthy Days', 'Very Unhealthy Days', 'Hazardous Days',
'Median AQI', 'Days CO', 'Days NO2', 'Days Ozone', 'Days SO2',
'Days PM2.5', 'Days PM10', 
'Latitude', 'Longitude'

The 2nd dataset is "US County Data of Center for Disease Control and Prevention" 
https://chronicdata.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2020-releas/i46a-9kgh

Data includes this columns:
'StateDesc', 'CountyName', 'TotalPopulation', 'CASTHMA_AdjPrev'

'CASTHMA_AdjPrev' is a target value for prediction. 
It's a prevalence of asthma in % for this area adjusted to age.
Min value: 7.1%, mean value: 9.83%, max value: 15.4%

Note:
I use data only for 2016 of the first dataset, because my second dataset has data only for - 2017 
Why not 2017 and 2017? 
Because matching of 2016 and 2017 gives better RMSE. I
It means If you move to the place with bad air quality, you will get your asthma only next year :)

### Dependency and enviroment management and run
README says how to install the dependencies and how to activate the env

### Containerization and run
Dockerfile is provided and README describes how to build a contained and how to run it

### Cloud deployment
Docs describe clearly (with code) how to deploy the service to the cloud
There's code for deployment and a public endpoint that could be tested


### Deliverables

For this project, you repository/folder should contain the following:

* `README.md` with
  * Description of the problem
  * Describing this problem and explaining how a model could be used
  * Instructions on how to run the project
* Notebook (suggested name - `notebook.ipynb`) with
  * Data preparation and data clearning
  * EDA, feature importance analysis
  * Model selection process and parameter tuning
* Script `train.py` (suggested name)
  * Training the final model
  * Saving it to a file (e.g. pickle)
* Script `predict.py` (suggested name)
  * Loading the model
  * Serving it via a web serice (e.g. with Flask)
* `Pipenv` and `Pipenv.lock`
  * or equivalents: conda environment file, requirements.txt or pyproject.toml
* `Dockerfile` for running the service


