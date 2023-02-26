import requests
import json
from pprint import pprint


params = {
    "api_key": "",
    "country": "de",
    "year": 2014,
    "mount": 12,
    "day": 31

}
r = requests.get('https://calendarific.com/api/v2/holidays/', params)

try:
    content = r.json()

except json.decoder.JSONDecodeError:
    print("incorrect format")
else:
    print(content)
