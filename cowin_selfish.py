#!/usr/bin/python

import os
import requests
import time
from datetime import datetime, timedelta
import argparse
from sys import platform

is_windows = False
# Speech dispatcher
speech_dispatcher = 'say' # for Mac
if 'linux' in platform:
    speech_dispatcher = 'spd-say'
if 'window' in platform:
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    is_windows = True


def speakPls(data):
           if is_windows:
               speak.Speak(str(data))
           else:
               os.system('{} "{}"'.format(speech_dispatcher, data))

# Tomorrow

default_age_limit = 18
default_fee_type = 'paid'

# Arguments parser
ap = argparse.ArgumentParser()
ap.add_argument("-dist", "--district-id", required=True, help="District ID for your district(you will have to find this id from cowin website)")
ap.add_argument("-age", "--age-limit", required=False, help="Age limit, 18 or 45? Defaults to 18", default=default_age_limit)
ap.add_argument("-fee", "--fee-type", required=False, help="Fee Type, free or paid? Defaults to Paid", default=default_fee_type)
args = vars(ap.parse_args())

district_id = 294
age_limit = 45
fee_type = 'Free'
vaccine = 'COVISHIELD'

done = False
while not done:
    for i in range(10):	
	    tomorrow = datetime.today() + timedelta(9+i)
	    tomorrow = tomorrow.strftime("%d-%m-%Y")
	    resp = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(district_id, tomorrow), 
				headers={
				    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
				    "accept": "application/json"
				}
		   )
	    resp = resp.json()
	    sessions = resp.get('sessions', [])
	    print ("Vaccine dila de bhagwan on ", tomorrow , "!")
	    #print([session for session in sessions if session.get('vaccine') == 'COVISHIELD'])
	    pincodes = [session.get('pincode') for session in sessions 
			if 
			#session.get('min_age_limit') == age_limit and 
			#session.get('fee_type') == fee_type and 
			session.get('vaccine') == 'COVISHIELD' and 
			session.get('available_capacity') > 0
			]
	    if pincodes:
	       print (pincodes)
	       #speakPls(pincode)
	       break    
    time.sleep(10)
os.system('{} "your program has finished"'.format(speech_dispatcher))
