import os
import json

leaked_pipes = []
new_leaked = []
arr = [1, 2]
with open('./datasets/pipes.json', 'r') as f:
    data = json.load(f)
    for ob in data['features']:
        # print(ob['geometry']['coordinates'])
        leaked_pipes.append(ob['geometry']['coordinates'])
        print(ob['geometry']['coordinates'])

# print(leaked_pipes)

for l in leaked_pipes:
    new_leaked.append([l[1], l[0]])

    new_leaked.append(arr)
    print(new_leaked)
