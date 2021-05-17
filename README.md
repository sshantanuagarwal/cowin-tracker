cowin-alert-sound-on
Keep sound on! The script announces PIN code when vaccine slot are available in your district on the next day. You should keep it running in the background.

For all the options:

python cowin.py -h
Command to run:

python cowin.py -dist <district_id>
eg, for Bangalore's BBMP district:

python cowin.py -dist 294
(294 is district id for Bangalore’s BBMP district)

Age group (default 18):

python cowin.py -dist 294 -age 45
python cowin.py -dist 294 -age 18
How to get district ID?

Get state ID from this curl command:
curl -X GET "https://cdn-api.co-vin.in/api/v2/admin/location/states" -H "accept: application/json" -H "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
Get district IDs by substituting state ID here:
curl -X GET "https://cdn-api.co-vin.in/api/v2/admin/location/districts/<state_id>" -H "accept: application/json" -H "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
eg for Karnataka (state id 16):

curl -X GET "https://cdn-api.co-vin.in/api/v2/admin/location/districts/16" -H "accept: application/json" -H "user-agent: Mozilla/5.0 (Macintosh ; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
Supported OS: Linux and Mac
