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
To install the dependencies and activate the env execute on linux:

#pipenv install scikit-learn==1.0 numpy flask gunicorn
#pipenv run gunicorn --bind 0.0.0.0:9696 predict:app


Also you can run pre-installed jupyter-notebook for better UI
#jupyter-notebook


Don't forget to clone project from git

#git clone https://github.com/aljeks/air-quality-and-asthma.git

Then just open address http://localhost:8888/ in your browser (jupyter-notebook or Anaconda should be up)
And enjoy /air-quality-and-asthma/notebook.ipynb

### Containerization and run
Dockerfile is provided with git project

To build docker container run:
#sudo docker build -t predict .

To run just builded container run:
#sudo docker run -it --rm -p 9696:9696 predict


### Cloud deployment

At first you have to get your AWS cloud machine.
Read more about this here https://mlbookcamp.com/article/aws and here https://mlbookcamp.com/article/aws-ec2
Don't forget to setup security settings in AWS console and open TCP 9696 port

Using address of your server navigate there

#ssh -i "jupiter.pem" ubuntu@ec2-18-222-227-70.us-east-2.compute.amazonaws.com

If you on your AWS ec2 server just clone your project from git

#git clone https://github.com/aljeks/air-quality-and-asthma.git

Then build docker container with all files provided:
#sudo docker build -t predict .

And finally run docker instance
#sudo docker run -d --rm -p 9696:9696 predict

(Optional) If you want to get inside container for some reason run it like
#sudo docker run -it --rm --entrypoint=bash predict

After tis you can sen a request to the cloud via jupiter notebook 'air-quality-and-asthma/notebook.ipynb'
It's in the bottom of file with label: 'Test example with request to AWS cloud service'

Or just run this curl from any terminal:
#
curl --location --request POST 'http://ec2-18-222-227-70.us-east-2.compute.amazonaws.com:9696/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
   "state":"nevada",
   "county":"clark",
   "days_with_aqi":366,
   "good_days":125,
   "moderate_days":215,
   "unhealthy_for_sensitive_groups_days":25,
   "unhealthy_days":0,
   "very_unhealthy_days":1,
   "hazardous_days":0,
   "median_aqi":58,
   "days_co":0,
   "days_no2":27,
   "days_ozone":1,
   "days_so2":0,
   "days_pm2.5":114,
   "days_pm10":6,
   "latitude":36.569333,
   "longitude":-115.676651,
   "totalpopulation":223647
}'




