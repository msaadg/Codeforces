import random
def read_input_file(input_filename):
  with open(input_filename, 'r') as file:
    data = file.readlines()
  return data

def write_output_file(output_filename, results):
  with open(output_filename, 'w') as file:
    for i, result in enumerate(results, 1):
      file.write(f"Case #{i}: {result}\n")

def solve(data):
  results = []
  idx = 0
  num_cases = int(data[idx])
  idx += 1

  for __ in range(num_cases):
    n = int(data[idx])
    idx += 1

    ants = []
    for i in range(n):
      ants.append(list(map(int, data[idx].split())))
      idx += 1
    
    p = 0
    for i in range(40):
      rnd1 = random.choice(ants)
      rnd2 = random.choice(ants)

      while rnd1 == rnd2:
        rnd2 = random.choice(ants)

      if rnd1[0] == rnd2[0]:
        m = 10 ** 10
      else:
        m = (rnd2[1] - rnd1[1]) / (rnd2[0] - rnd1[0])
      c = rnd1[1] - m * rnd1[0]

      curp = 0
      for ant in ants:
        x, y = ant
        if y == m * x + c:
          curp += 1
      
      p = max(p, curp)
    results.append(2 * (n - p))
  return results

if __name__ == "__main__":
  input_filename = "s.txt"
  output_filename = "output.txt"
  
  input_data = read_input_file(input_filename)
  output_data = solve(input_data)
  write_output_file(output_filename, output_data)
