import urllib.request, json, ssl, time

myKey = "7cc441d4c80dc500e03786e94fd81402"
url = 'https://api.themoviedb.org/3/movie/{0}?api_key={1}&append_to_response=credits'

data = open("movie_data.txt", "r")
data_string = data.read()
data.close()
j = json.loads(data_string)


THE_ALMIGHTY_GRAPH = {}


N=0
now = time.time()
future = now + 10
calls_made = 0
# for i in range(30):
#     page = j[i]
for page in j:
    print(N)
    N+=1
    for movie in page['results']:
        if calls_made > 38 and time.time() < future:
            time.sleep(max(0,future - time.time()))
            now = time.time()
            future = now + 10
            calls_made = 0
        elif time.time() > future:
            now = time.time()
            future = now + 10
            calls_made = 0

        calls_made += 1
        specific_url = url.format(movie['id'], myKey)
        with urllib.request.urlopen(specific_url) as cur_url:
            movie = json.loads(cur_url.read().decode())
            actor_list = [actor['name'] for actor in movie['credits']['cast']]

            for actor in actor_list:
                if actor not in THE_ALMIGHTY_GRAPH:
                    THE_ALMIGHTY_GRAPH[actor] = {}

                for connection in actor_list:
                    if connection != actor:
                        if connection not in THE_ALMIGHTY_GRAPH[actor]:
                            THE_ALMIGHTY_GRAPH[actor][connection] = 0
                        THE_ALMIGHTY_GRAPH[actor][connection] += 1


# for actor in THE_ALMIGHTY_GRAPH:
#     THE_ALMIGHTY_GRAPH[actor] = list(THE_ALMIGHTY_GRAPH[actor])

with open('cast_graph.json', 'w') as f:
    json.dump(THE_ALMIGHTY_GRAPH, f)


cast_data = open("cast_graph.json", "r")
cast_data_string = cast_data.read()
cast_data.close()
ALMIGHTY_GRAPH_RELOADED = json.loads(cast_data_string)