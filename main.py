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
movie_list = json.loads(response.content)

movie_results = movie_list['results']

for i in range(2, 40):
    page_num = i
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'include_adult': 'false',
        'include_video': 'false',
        'page': page_num
    }
    response = requests.get(url, params=params)
    movie_list = json.loads(response.content)
    movie_results += movie_list['results']

df = pd.DataFrame(movie_results)
df = df.drop(labels=['adult','backdrop_path','poster_path','video'], axis=1)
liked = np.random.rand(len(df)) < 0.05
df['liked'] = liked
# msk = np.random.rand(len(df)) < 0.8
# train = df[msk]
# test = df[~msk]

