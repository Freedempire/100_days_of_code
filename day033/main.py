from datetime import datetime, timezone
import smtplib
import time

import requests


def is_night(lat, lng):
    # to find latitude and longitude of a place from https://www.latlong.net/
    
    SUNRISE_SUNSET_API = 'https://api.sunrise-sunset.org/json'

    # get current local time with tzinfo attribute 
    now_tz = datetime.now().astimezone()
    # get current date in local timezone
    current_date_tz = now_tz.date()
    # get current timedate in utc timezone
    current_time_utc = now_tz.astimezone(timezone.utc)

    sunrise_sunset_api_params = {
        'lat': lat,
        'lng': lng,
        'date': current_date_tz,
        'formatted': 0
    }

    sunrise_sunset_dict = requests.get(SUNRISE_SUNSET_API, sunrise_sunset_api_params).json()['results']
    sunrise_time_utc_str = sunrise_sunset_dict['sunrise']
    sunset_time_utc_str = sunrise_sunset_dict['sunset']
    # get a datetime corresponding to date_string, parsed according to format
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
    # https://docs.python.org/3/library/time.html#time.strftime
    sunrise_time_utc = datetime.strptime(sunrise_time_utc_str, '%Y-%m-%dT%H:%M:%S%z')
    sunset_time_utc = datetime.strptime(sunset_time_utc_str, '%Y-%m-%dT%H:%M:%S%z')

    return current_time_utc > sunset_time_utc or current_time_utc < sunrise_time_utc


def is_iss_overhead(tolerance=5):
    ISS_NOTIFY_API = 'http://api.open-notify.org/iss-now.json'

    response_iss = requests.get(ISS_NOTIFY_API)
    iss_position = response_iss.json()['iss_position']
    iss_lat, iss_lng = tuple(map(lambda x: float(x), iss_position.values()))
    if iss_lat - tolerance < MY_LAT < iss_lat + tolerance and iss_lng - tolerance < MY_LNG < iss_lng + tolerance:
        return True
    else:
        return False
    

def notify_by_email(host, email, password, msg):
    with smtplib.SMTP(host) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email, email, msg)


MY_LAT = -33.868820
MY_LNG = 151.209290

HOST = 'smtp.gmail.com'
EMAIL = 'tony@gmail.com'
PASSWORD = '348748eikfdadhfg'
MSG = 'Subject:ISS Speculation Notification\n\nLook up 👆! The ISS is currently overhead.'

while True:
    if is_night(MY_LAT, MY_LNG) and is_iss_overhead():
        print('Look! The International Space Station is currently over your head!')
        notify_by_email(HOST, EMAIL, PASSWORD, MSG)
    time.sleep(600)
