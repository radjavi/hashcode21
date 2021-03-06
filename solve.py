#from sortedcollections import ValueSortedDict
#from sortedcontainers import SortedList
from collections import defaultdict
import numpy as np

# Solver that takes an input as a file object,
# and returns the output as a string
def solve(inp):
    return solve1(inp)

def solve1(inp):
    line1 = [int(x) for x in inp.readline().strip().split(' ')]
    D = line1[0]
    I = line1[1]
    S = line1[2]
    V = line1[3]
    F = line1[4]

    s = 0
    streets = {}
    intersections = {}
    # Street descriptions
    while s < S:
        line = inp.readline().strip().split(' ')
        B = int(line[0])
        E = int(line[1])
        street_name = line[2]
        L = int(line[3])
        streets[street_name] = {
            "start": B,
            "end": E,
            "length": L,
            'weight' : 0
        }
        if B not in intersections:
            intersections[B] = {
                "green_lights": [],
                "incoming": [],
                "outgoing": [street_name],
            }
        else:
            intersections[B]["outgoing"].append(street_name)
        if E not in intersections:
            intersections[E] = {
                "green_lights": [],
                "incoming": [street_name],
                "outgoing": [],
            }
        else:
            intersections[E]["incoming"].append(street_name)
        s += 1

    v = 0
    street_count = defaultdict(int)
    #cars = SortedList(key=lambda x: len(x))
    # Paths of each car
    while v < V:
        line = inp.readline().strip().split(' ')
        P = int(line[0])
        # car = []

        for p in range(1,P):
            #print([next_p for next_p in range(p,P)])
            path_weight = np.sum([streets[line[next_p]]['length'] for next_p in range(p,P)])

            incoming_weight = 0
            inc_inter = intersections[streets[line[p]]['start']]['incoming']
            for inc in inc_inter:
               incoming_weight += 1/streets[inc]['length']

            street_count[line[p]] += 1/P

        #    car.append(line[p])
        # cars.add(car)

        v += 1

    print(len(street_count))
    #print(cars)
    #print(starting_street_count)

    for intersection, v in intersections.items():
        sum_incoming_weights = sum([street_count[incoming] for incoming in v["incoming"]])
        intersections[intersection]["sum_incoming_weights"] = sum_incoming_weights

    for intersection, v in intersections.items():
        for incoming in v["incoming"]:
            weight = 0
            if v["sum_incoming_weights"] != 0:
                weight = street_count[incoming] / v["sum_incoming_weights"]
            streets[incoming]["weight"] += weight
            # for v_tmp in intersections[streets[incoming]["start"]]['incoming']:
            #   streets[v_tmp]['weight'] += streets[incoming]['length']/D

    for intersection, v in intersections.items():

      for incoming in v["incoming"]:
         v["green_lights"].append({
            "name": incoming,
            "duration": np.min([D, np.max([int(streets[incoming]["weight"] * np.min([D, 10])), 1])]),
         })

    out_str = f'{len(intersections)}\n'
    for intersection in intersections:
        out_str += f'{intersection}\n'
        out_str += f'{len(intersections[intersection]["green_lights"])}\n'
        for green_light in intersections[intersection]["green_lights"]:
            out_str += f'{green_light["name"]}'
            out_str += ' '
            out_str += f'{green_light["duration"]}'
            out_str += '\n'

    return out_str
