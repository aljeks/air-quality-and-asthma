
import requests

url = "http://localhost:9696/predict"

place = {'state': 'nevada',
 'county': 'clark',
 'days_with_aqi': 366,
 'good_days': 125,
 'moderate_days': 215,
 'unhealthy_for_sensitive_groups_days': 25,
 'unhealthy_days': 0,
 'very_unhealthy_days': 1,
 'hazardous_days': 0,
 'median_aqi': 58,
 'days_co': 0,
 'days_no2': 27,
 'days_ozone': 219,
 'days_so2': 0,
 'days_pm2.5': 114,
 'days_pm10': 6,
 'latitude': 36.569333,
 'longitude': -115.676651,
 'totalpopulation': 2231647}
 
respose = requests.post(url, json=place).json()
print("Prevalece of Asthma in % for this place. (min: 7.1, mean: 9.83, max: 15.4)")
print(respose)

