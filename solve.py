from sortedcollections import ValueSortedDict

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
    starting_street_count = ValueSortedDict()
    cars = []
    # Paths of each car
    while v < V:
        line = inp.readline().strip().split(' ')
        P = int(line[0])
        car = []
        for p in range(P):
           car.append(line[p])
        cars.append(car)
        if line[1] not in starting_street_count:
            starting_street_count[line[1]] = 1
        else:
            starting_street_count[line[1]] += 1
        v += 1

    print(starting_street_count)
    
    for starting_street in starting_street_count.__reversed__():
        E = streets[starting_street]["end"]
        duration = starting_street_count[starting_street]
        if len(intersections[E]["green_lights"]) == 0:
            intersections[E]["green_lights"].append({
                "name": starting_street,
                "duration": D,
            })

    for intersection in intersections:
        if not intersections[intersection]["green_lights"]:
            intersections[intersection]["green_lights"].append({
                "name": intersections[intersection]["incoming"][0],
                "duration": D,
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
