# Solver that takes an input as a file object,
# and returns the output as a string
def solve(inp):
  return pizza_iman(inp)

# Pizza solver that takes an input as a file object,
# and returns the output as a string
def pizza(inp):
  line1 = [int(x) for x in inp.readline().strip().split(' ')]
  M = line1[0]
  T2 = line1[1]
  T3 = line1[2]
  T4 = line1[3]

  # TODO: Solution

  return ''

# A simple, but not so smart, pizza solver.
def pizza_iman(inp):
  line1 = [int(x) for x in inp.readline().strip().split(' ')]
  M = line1[0]
  T2 = line1[1]
  T3 = line1[2]
  T4 = line1[3]
  
  deliveries = []
  i = 0
  while i <= M:
    nrPizzas = 0
    if T4 > 1 and M - i >= 4:
      nrPizzas = 4
      T4 -= 1
    elif T3 > 1 and M - i >= 3:
      nrPizzas = 3
      T3 -= 1
    elif T2 > 1 and M - i >= 2:
      nrPizzas = 2
      T2 -= 1
    pizzas = []
    for j in range(nrPizzas):
      pizzas.append(i + j)
    if nrPizzas == 0:
      break
    deliveries.append(pizzas)
    i += nrPizzas

  out_str = f'{len(deliveries)}\n'
  for delivery in deliveries:
    out_str += f'{len(delivery)}'
    for pizza in delivery:
      out_str += f' {pizza}'
    out_str += '\n'

  return out_str