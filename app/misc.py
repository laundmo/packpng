import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

s = requests.Session()

retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])

s.mount('http://', HTTPAdapter(max_retries=retries))
s.mount('https://', HTTPAdapter(max_retries=retries))

def get_contributors_json():
    response = s.get("https://api.github.com/repos/laundmo/packpng/stats/contributors")
    contributors = response.json()
    contributors = sorted(contributors, key=lambda x: x['total'], reverse=True)
    for contrib in contributors:
        added = sum([w['a'] for w in contrib['weeks']])
        deleted = sum([w['d'] for w in contrib['weeks']])
        contrib["added"] = added
        contrib["deleted"] = deleted
    return contributors