import pandas as pd;
import numpy as np;
import matplotlib as plot;

import json
import requests

api_key = '7cc441d4c80dc500e03786e94fd81402'

url = 'https://api.themoviedb.org/3/discover/movie'
page_num = 1
params = {
    'api_key': api_key,
    'language': 'en-US',
    'sort_by': 'popularity.desc',
    'include_adult': 'false',
    'include_video': 'false',
    'page': page_num

}
response = requests.get(url, params = params)
print(response)
movie_list = json.loads(response.content)

for movie in movie_list['results']:
    print(movie['title'])