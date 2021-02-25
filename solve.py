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
    # Street descriptions
    while s < S:
        line = inp.readline().strip().split(' ')
        B = int(line[0])
        E = int(line[1])
        street_name = line[2]
        L = int(line[3])
        s += 1
    
    v = 0
    # Paths of each car
    while v < V:
        line = inp.readline().strip().split(' ')
        P = int(line[0])
        for p in range(P):
            street = line[p]
        v += 1

    intersections = {}

    out_str = f'{len(intersections)}\n'
    for intersection in intersections:
        out_str += f'{intersection.id}\n'
        out_str += f'{intersection.nr_incoming}\n'
        for green_light in intersection.green_lights:
            out_str += f'{green_light.name}'
            out_str += ' '
            out_str += f'{green_light.duration}'
            out_str += '\n'

    return ""
