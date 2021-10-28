# air-quality-and-asthma
ML project - model of air quality data with prediction of asthma prevalence based on data for all counties of USA

Two datasets are merged in this project "Air Quality" and "Asthma prevalence"

The 1st dataset is "1980-2021 Yearly Air Quality Index from the EPA" 
https://www.kaggle.com/threnjen/40-years-of-air-quality-index-from-the-epa-yearly



The 2nd dataset is "PLACES: County Data (GIS Friendly Format), 2020 release" https://chronicdata.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2020-releas/i46a-9kgh

I use data only for one year 2016, because my second dataset has data only for - 2017 
Why not 2017 and 2017? 
Because 2016 - 2017 gives better RMSE. I
t means If you move to the place with bad air quality, you will get your asthma only next year :)



* Thinking of a problem that's interesting for you and finding a dataset for that
* Describing this problem and explaining how a model could be used
* Preparing the data and doing EDA, analyzing important features
* Training multiple models, tuning their performance and selecting the best model
* Exporting the notebook into a script
* Putting your model into a web service and deploying it locally with docker
* Bonus points for deploying the service to the cloud


### Datasets

* https://www.kaggle.com/datasets and https://www.kaggle.com/competitions
* https://archive.ics.uci.edu/ml/index.php
* https://data.europa.eu/en
* https://www.openml.org/search?type=data
* Add more data here!

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


