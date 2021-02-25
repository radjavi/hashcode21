from collections import defaultdict


class Intersection(object):
    def __init__(self, id, inc_streets, streets):
        self.id = id
        self.inc_streets = inc_streets
        self.streets = []
        self.queue = {}  # streetname -> list(car.id)

    def append(self, street):
        self.streets.append(street)


class Car(object):
    def __init__(self, id, curr, time, path):
        self.id = id
        self.curr = curr  # int
        self.time = time  # int
        self.path = path  # str[]


def score(in_str, out_str):
    in_str.seek(0)
    out_str = out_str.split('\n')
    line1 = [int(x) for x in in_str.readline().strip().split(' ')]
    D = line1[0]
    I = line1[1]
    S = line1[2]
    V = line1[3]
    F = line1[4]

    s = 0
    world = {}
    # Street descriptions
    while s < S:
        line = in_str.readline().strip().split(' ')
        B = int(line[0])
        E = int(line[1])
        street_name = line[2]
        L = int(line[3])
        s += 1
        world[street_name] = (B, E)

    v = 0
    cars = dict()
    queues = defaultdict(list)
    # Paths of each car
    while v < V:
        line = in_str.readline().strip().split(' ')
        P = int(line[0])
        path = line[1:]
        for p in range(P):
            street = line[p]

        cars[v] = Car(v, 0, 0, path)

        v += 1

    map = dict()

    intersections = int(out_str[0].strip())
    idx = 1
    while idx < len(out_str):
        id = int(out_str[idx].strip())
        inc_streets = int(out_str[idx+1])
        intersection = Intersection(id, inc_streets, [])

        for j in range(inc_streets):
            street_name, duration = out_str[idx+j+2].split(' ')
            intersection.append((street_name, duration))

        map[id] = intersection
        idx += inc_streets + 2

    # Init all queues
    for car in cars.values():
        queues[car.path[car.curr]].append(car.id)

    # This was a waste of time, let's just leave the code here