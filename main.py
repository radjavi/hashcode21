import solve, score
import argparse

def hashcode(in_file, out_file):
  with open(in_file, "r") as inp, open(out_file, "w") as out:
    # Call appropriate solver
    out_str = solve.solve(inp)
    # Create output file
    out.write(out_str)
    print(f'DONE: {out_file}, SCORE: {score.score(out_str)}')

if __name__ == '__main__':
  hashcode("in/a_example.in", "out/a_out")
  hashcode("in/b_little_bit_of_everything.in", "out/b_out")
  hashcode("in/c_many_ingredients.in", "out/c_out")
  hashcode("in/d_many_pizzas.in", "out/d_out")
  hashcode("in/e_many_teams.in", "out/e_out")